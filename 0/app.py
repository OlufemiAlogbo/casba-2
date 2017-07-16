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
from flask import Flask, render_template, url_for, request, redirect
import ibm_db
import datetime

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

port = os.getenv('PORT', '5000')
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=int(port), debug=True)
