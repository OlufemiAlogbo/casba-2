# Copyright 2015 IBM Corp. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
from flask import Flask, render_template, url_for, request, redirect, session
import ibm_db
import datetime
import json
from flask_socketio import SocketIO, emit
from watson_developer_cloud import ConversationV1
import urllib
import hashlib
from flutterwave import Flutterwave

app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'dinosaurs'

# DashDB
#Enter the values for you database connection
dsn_driver = "IBM DB2 ODBC DRIVER"
dsn_database = "BLUDB"
dsn_hostname = "dashdb-entry-yp-lon02-01.services.eu-gb.bluemix.net"
dsn_port = "50000"
dsn_protocol = "TCPIP"
dsn_uid = "dash8359"
dsn_pwd = "0e_yj2GJ_BLj"

dsn = (
    "DRIVER={{IBM DB2 ODBC DRIVER}};"
    "DATABASE={0};"
    "HOSTNAME={1};"
    "PORT={2};"
    "PROTOCOL=TCPIP;"
    "UID={3};"
    "PWD={4};").format(dsn_database, dsn_hostname, dsn_port, dsn_uid, dsn_pwd)

conn = ibm_db.connect(dsn, "", "")

# SocketIO
socketio = SocketIO(app, async_mode='eventlet')
thread = None

# Watson Conversation
conversation = ConversationV1(
  username="4a23fe86-b0f6-4e1c-8dab-e707c2547b8c",
  password="0qO4k0TbbBsf",
  version='2017-05-26'
)

workspace_id = 'f7570f32-c417-41fe-b5b4-c7db19c893d1'

context = {}
last_response = ""

# Flutterwave
flw = Flutterwave("", "", {"debug": True})

user = "..."

# Views
@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'email' in request.form:
            sql = "SELECT * FROM CUSTOMER ORDER BY ID DESC fetch first 1 row only"
            stmt = ibm_db.exec_immediate(conn, sql)
            customer = 1
            while ibm_db.fetch_row(stmt) != False:
                customer = customer + int(ibm_db.result(stmt, "ID"))
            sql = "INSERT INTO CUSTOMER (ID, EMAIL, TOC) VALUES (?, ?, ?)"
            stmt = ibm_db.prepare(conn, sql)
            param = customer, request.form["email"], datetime.date.today(),
            ibm_db.execute(stmt, param)
            return redirect(url_for('index'))
    else:
      return render_template('index.html')

@app.route('/chat')
def chat():
    user_ip = request.remote_addr
    user_agent = request.headers.get('User-Agent')
    session['unique_conversation_id'] = str(user_ip) + "__" + str(user_agent)
    context["conversation_id"] = str(hashlib.sha256(session['unique_conversation_id'].encode('utf-8')).hexdigest())
    return render_template('chat.html', async_mode=socketio.async_mode)

# Websocket
@socketio.on('my event')
def handleMessage(message):
    from_human_message = str(message["data"])
    global context
    global response
    global bvn_response
    global otp_response
    global user

    intent = " "
    entity = " "
    form = " "
    bot_response = "...."
    responseMessage = "...."
    try:
        context["conversation_id"] = str(hashlib.sha256(session['unique_conversation_id'].encode('utf-8')).hexdigest())
        response = conversation.message(workspace_id=workspace_id, message_input={'text': urllib.unquote(from_human_message)}, context=context)
        context = response["context"]

        if len(json.loads(json.dumps(response, indent=2))['intents']) > 0:
            intent = json.loads(json.dumps(response, indent=2))['intents'][0]['intent']
            if intent == "hello":
                try:
                    bot_response = ' '.join(response["output"]["text"])
                except Exception as ex:
                    print("exception :( ", ex)
            elif intent == "add_card":
                print user
                form = "addcard"
                try:
                    bot_response = ' '.join(response["output"]["text"])
                except Exception as ex:
                    print("exception :( ", ex)
            else:
                try:
                    bot_response = ' '.join(response["output"]["text"])
                except Exception as ex:
                    print("exception :( ", ex)
        elif len(json.loads(json.dumps(response, indent=2))['entities']) > 0:
            entity = json.loads(json.dumps(response, indent=2))['entities'][0]['value']
            if entity == "BVN":
                bvn = str(json.loads(json.dumps(response, indent=2))['context']['bvn'].split()[1])
                verifyUsing = "Voice"
                country = "NGN"

                r = flw.bvn.verify(bvn, verifyUsing, country)
                bvn_response = json.loads("{0}".format(r.text))
                responseMessage = bvn_response["data"]
                if "Successful" in str(responseMessage["responseMessage"]):
                    if len(json.loads(json.dumps(response, indent=2))['output']['text']) != 0:
                        try:
                            bot_response = ' '.join(response["output"]["text"])
                        except Exception as ex:
                            print("exception :( ", ex)
                elif "Invalid" in str(responseMessage["responseMessage"]):
                    try:
                        bot_response = "Invalid BVN, Please try again with BVN + space + 11 digit number"
                    except Exception as ex:
                        print("exception :( ", ex)
                else:
                    try:
                        bot_response = "Service unavailable, Please try again in 30 mins"
                    except Exception as ex:
                        print("exception :( ", ex)
            elif json.loads(json.dumps(response, indent=2))['entities'][0]['entity'] == "bool":
                if 'payment' in message:
                    card = message["payment"]
                    sql = "SELECT * FROM SIGNUP WHERE CARDNUMBER = ?"
                    stmt = ibm_db.prepare(conn, sql)
                    param = card["number"],
                    ibm_db.execute(stmt, param)
                    if ibm_db.fetch_row(stmt) != True:
                        sql = "SELECT * FROM SIGNUP WHERE BVN = ? fetch first 1 row only"
                        stmt = ibm_db.prepare(conn, sql)
                        param = card["bvn"],
                        ibm_db.execute(stmt, param)
                        while ibm_db.fetch_row(stmt) != False:
                            sql = "UPDATE SIGNUP SET CARDNUMBER = ?, CARDTYPE = ?, EXPIRY = ?, CVC = ? WHERE BVN = ?"
                            stmt = ibm_db.prepare(conn, sql)
                            param = card["number"], card["type"], card["expiry"], card["cvc"], card["bvn"],
                            ibm_db.execute(stmt, param)
                            if len(json.loads(json.dumps(response, indent=2))['output']['text']) != 0:
                                try:
                                    bot_response = ' '.join(response["output"]["text"])
                                except Exception as ex:
                                    print("exception :( ", ex)
                    else:
                        try:
                            bot_response = " ".join([str(ibm_db.result(stmt, "FIRSTNAME")), ", You already have payment card on record!"])
                        except Exception as ex:
                            print("exception :( ", ex)
                else:
                    if len(json.loads(json.dumps(response, indent=2))['output']['text']) != 0:
                        try:
                            bot_response = ' '.join(response["output"]["text"])
                        except Exception as ex:
                            print("exception :( ", ex)
            elif len(json.loads(json.dumps(response, indent=2))['entities'][0]['value']) == 5:
                if len(json.loads(json.dumps(response, indent=2))['context']['otp']) == 5:
                    bvn = str(json.loads(json.dumps(response, indent=2))['context']['bvn'].split()[1])
                    otp = str(json.loads(json.dumps(response, indent=2))['context']['otp'])
                    transactionReference = str(bvn_response["data"]["transactionReference"])
                    country = "NGN"

                    r = flw.bvn.validate(bvn, otp, transactionReference, country)
                    otp_response = json.loads("{0}".format(r.text))
                    user = otp_response["data"]
                    if user["bvn"] != "":
                        sql = "SELECT * FROM SIGNUP WHERE BVN = ?"
                        stmt = ibm_db.prepare(conn, sql)
                        param = user["bvn"],
                        ibm_db.execute(stmt, param)
                        if ibm_db.fetch_row(stmt) != True:
                            sql = "SELECT * FROM SIGNUP ORDER BY ID DESC fetch first 1 row only"
                            stmt = ibm_db.exec_immediate(conn, sql)
                            user["id"] = 1
                            while ibm_db.fetch_row(stmt) != False:
                                user["id"] = 1 + int(ibm_db.result(stmt, "ID"))
                            sql = "INSERT INTO SIGNUP (ID, BVN, LASTNAME, FIRSTNAME, PHONENUMBER, DATEOFBIRTH, DOC) VALUES (?, ?, ?, ?, ?, ?, ?)"
                            stmt = ibm_db.prepare(conn, sql)
                            param = user["id"], user["bvn"], user["lastName"], user["firstName"], user["phoneNumber"], user["dateOfBirth"], datetime.date.today(),
                            ibm_db.execute(stmt, param)
                            form = "signup"
                            if len(json.loads(json.dumps(response, indent=2))['output']['text']) != 0:
                                try:
                                    bot_response = ' '.join(response["output"]["text"])
                                except Exception as ex:
                                    print("exception :( ", ex)
                        else:
                            try:
                                bot_response = "You are already registered!"
                            except Exception as ex:
                                print("exception :( ", ex)
                    else:
                        try:
                            bot_response = "OTP not verified! Please start signup again..."
                        except Exception as ex:
                            print("exception :( ", ex)
                else:
                    try:
                        bot_response = "OTP must be 5 digits! Please start signup again..."
                    except Exception as ex:
                        print("exception :( ", ex)
        else:
            if len(json.loads(json.dumps(response, indent=2))['output']['text']) != 0:
                try:
                    bot_response = ' '.join(response["output"]["text"])
                except Exception as ex:
                    print("exception :( ", ex)

    except Exception as ex:
        print("watson exception :( ", ex)

    print("\n\nBOT SAYS: " + json.dumps(response))

    # sometimes the fucking bot doesn't answer what it should.
    if len(bot_response) < 2:
        bot_response = "I couldn't understand that. You can type 'help' for example"

    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my response', {'data': bot_response, 'intent': intent, 'entity': entity, 'user': user, 'form': form, 'count': session['receive_count']})

    conversations = {'data': bot_response, 'human': from_human_message, 'intent': intent, 'entity': entity, 'count': session['receive_count']}
    if 'data' in conversations:
        sql = "SELECT * FROM CONVERSATIONS ORDER BY ID DESC fetch first 1 row only"
        stmt = ibm_db.exec_immediate(conn, sql)
        conversations["id"] = 1
        while ibm_db.fetch_row(stmt) != False:
            conversations["id"] = conversations["id"] + int(ibm_db.result(stmt, "ID"))
        sql = "INSERT INTO CONVERSATIONS (ID, BOTMESSAGE, HUMANMESSAGE, INTENT, ENTITY, TOC) VALUES (?, ?, ?, ?, ?, ?)"
        stmt = ibm_db.prepare(conn, sql)
        param = conversations["id"], conversations["data"], conversations["human"], conversations["intent"], conversations["entity"], datetime.datetime.utcnow(),
        ibm_db.execute(stmt, param)

port = os.getenv('PORT', '5000')
if __name__ == "__main__":
	#app.run(host='0.0.0.0', port=int(port), debug=True)
	socketio.run(app, host='0.0.0.0', port=int(port), debug=True)
