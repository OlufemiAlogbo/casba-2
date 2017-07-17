// Build send message with HTML
function buildMessageSend(text) {
  var element = document.createElement('div');

  element.classList.add('message', 'sent');

  element.innerHTML = text +
  '<span class="metadata">' +
  '<span class="time">' + moment().format('h:mm A') + '</span>'
  '</span>';

  return element;
}

// Build receive message with HTML
function buildMessageRecieve(text) {
  var element = document.createElement('div');

  element.classList.add('message', 'received');

  element.innerHTML = text +
  '<span class="metadata">' +
  '<span class="time">' + moment().format('h:mm A') + '</span>'
  '</span>';

  return element;
}

// Build hello message attachment
function buildHelloAttachment() {
  var element = document.createElement('div');

  element.classList.add('message', 'attachment');

  element.innerHTML = '<div class="app-attachment">' +
    '<button type="submit" class="btn btn-primary btn-lg btn-md btn-sm btn-xs btn-chat" id="getstarted"><span class="glyphicon glyphicon-log-in"></span>    Get Started</button>' +
    '<button type="submit" class="btn btn-primary btn-lg btn-md btn-sm btn-xs btn-chat"><span class="glyphicon glyphicon-map-marker"></span>    Find ATM</button>' +
    '<button type="submit" class="btn btn-primary btn-lg btn-md btn-sm btn-xs btn-chat"><span class="glyphicon glyphicon-credit-card"></span>    Pay Bills</button>' +
  '</div>';

  return element;
}

// Build registered message attachment
function buildRegisteredAttachment() {
  var element = document.createElement('div');

  element.classList.add('message', 'attachment');

  element.innerHTML = '<div class="app-attachment">' +
    '<button type="submit" class="btn btn-primary btn-lg btn-md btn-sm btn-xs btn-chat" id="setupcard"><span class="glyphicon glyphicon-credit-card"></span>  Setup Card</button>' +
  '</div>';

  return element;
}

// Build setup message attachment
function buildSetupAttachment() {
  var element = document.createElement('div');

  element.classList.add('message', 'attachment');

  element.innerHTML = '<div class="app-attachment">' +
    '<a type="submit" class="btn btn-primary btn-lg btn-md btn-sm btn-xs btn-chat"><span class="glyphicon glyphicon-map-marker"></span>    Find ATM</a>' +
    '<a type="submit" class="btn btn-primary btn-lg btn-md btn-sm btn-xs btn-chat"><span class="glyphicon glyphicon-credit-card"></span>    Pay Bills</a>' +
  '</div>';

  return element;
}

// Build BVN Signup form
function buildSignupForm(user) {
  var element = document.createElement('div');

  element.classList.add('col-lg-6', 'col-md-6', 'col-sm-8', 'col-xs-10', 'col-lg-offset-3', 'col-md-offset-3', 'col-sm-offset-2', 'col-xs-offset-1', 'signupForm');

  element.innerHTML = '<div class="well well-lg well-md well-sm well-xs text-center">' +
    '<h1><small>Personal Info</small></h1>' +
    '<hr>' +
    '<div class="form-horizontal">' +
      '<div class="form-group">' +
        '<div class="col-lg-10 col-md-10 col-sm-10 col-xs-10 col-lg-offset-1 col-md-offset-1 col-sm-offset-1 col-xs-offset-1">' +
          '<input type="text" class="form-control text-center" value= ' + user.lastName + ' autofocus disabled>' +
        '</div>' +
      '</div>' +
      '<div class="form-group">' +
        '<div class="col-lg-10 col-md-10 col-sm-10 col-xs-10 col-lg-offset-1 col-md-offset-1 col-sm-offset-1 col-xs-offset-1">' +
          '<input type="text" class="form-control text-center" value= ' + user.firstName + ' autofocus disabled>' +
        '</div>' +
      '</div>' +
      '<div class="form-group">' +
        '<div class="col-lg-10 col-md-10 col-sm-10 col-xs-10 col-lg-offset-1 col-md-offset-1 col-sm-offset-1 col-xs-offset-1">' +
          '<input type="text" class="form-control text-center" value= ' + user.phoneNumber + ' autofocus disabled>' +
        '</div>' +
      '</div>' +
      '<div class="form-group">' +
        '<div class="col-lg-10 col-md-10 col-sm-10 col-xs-10 col-lg-offset-1 col-md-offset-1 col-sm-offset-1 col-xs-offset-1">' +
          '<input type="text" class="form-control text-center" value= ' + user.dateOfBirth + ' autofocus disabled>' +
        '</div>' +
      '</div>' +
      '<div class="form-group">' +
        '<div class="col-lg-10 col-md-10 col-sm-10 col-xs-10 col-lg-offset-1 col-md-offset-1 col-sm-offset-1 col-xs-offset-1">' +
          '<input type="text" class="form-control text-center" value= ' + user.bvn + ' autofocus disabled>' +
        '</div>' +
      '</div>' +
      '<div class="form-group">' +
        '<div class="col-lg-10 col-md-10 col-sm-10 col-xs-10 col-lg-offset-1 col-md-offset-1 col-sm-offset-1 col-xs-offset-1">' +
          '<button type="submit" class="btn btn-primary btn-lg btn-md btn-sm btn-xs btn-chat" id="signupForm"> Confirm </button>' +
        '</div>' +
      '</div>' +
    '</div>' +
  '</div>';

  return element;
}

// Build Card Setup form
function buildCardForm(user_arr) {
  var element = document.createElement('div');

  element.classList.add('col-lg-6', 'col-md-6', 'col-sm-8', 'col-xs-10', 'col-lg-offset-3', 'col-md-offset-3', 'col-sm-offset-2', 'col-xs-offset-1', 'addcardForm');

  element.innerHTML = '<div class="well well-lg well-md well-sm well-xs text-center">' +
    '<h1><small>Card Info</small></h1>' +
    '<hr>' +
    '<div class="form-horizontal">' +
      '<div class="form-group">' +
        '<div class="col-lg-10 col-md-10 col-sm-10 col-xs-10 col-lg-offset-1 col-md-offset-1 col-sm-offset-1 col-xs-offset-1">' +
          '<input type="text" id="inputBVN" class="form-control text-center" value= "' + user_arr[0] + '" autofocus disabled>' +
        '</div>' +
      '</div>' +
      '<div class="form-group">' +
        '<div class="col-lg-10 col-md-10 col-sm-10 col-xs-10 col-lg-offset-1 col-md-offset-1 col-sm-offset-1 col-xs-offset-1">' +
          '<input type="text" id="inputName" class="form-control text-center" value= "' + user_arr[1] + '" autofocus disabled>' +
        '</div>' +
      '</div>' +
      '<div class="form-group">' +
        '<div class="col-lg-8 col-md-8 col-sm-8 col-xs-8 col-lg-offset-2 col-md-offset-2 col-sm-offset-2 col-xs-offset-2">' +
          '<select class="form-control" id="inputType">' +
            '<option>Select CARD Type</option>' +
            '<option value="visa">Visa Card</option>' +
            '<option value="verve">Verve Card</option>' +
            '<option value="master">Master Card</option>' +
          '</select>' +
        '</div>' +
      '</div>' +
      '<div class="form-group">' +
        '<div class="col-lg-10 col-md-10 col-sm-10 col-xs-10 col-lg-offset-1 col-md-offset-1 col-sm-offset-1 col-xs-offset-1">' +
          '<input type="text" id="inputNumber" class="form-control text-center" placeholder="Enter Card Number xxxxxxxxxxxxxxxx" autofocus>' +
        '</div>' +
      '</div>' +
      '<div class="form-group form_datetime">' +
        '<div class="col-lg-8 col-md-8 col-sm-8 col-xs-8 col-lg-offset-2 col-md-offset-2 col-sm-offset-2 col-xs-offset-2 input-group">' +
          '<input class="form-control" id="inputExpiry" name="date" placeholder="MM/DD/YYY" type="text"/>' +
          '<div class="input-group-addon"><span class="glyphicon glyphicon-calendar"></span></div>' +
        '</div>' +
      '</div>' +
      '<div class="form-group">' +
        '<div class="col-lg-10 col-md-10 col-sm-10 col-xs-10 col-lg-offset-1 col-md-offset-1 col-sm-offset-1 col-xs-offset-1">' +
          '<input type="text" id="inputCVC" class="form-control text-center" placeholder="Enter CVC" autofocus >' +
        '</div>' +
      '</div>' +
      '<div class="form-group">' +
        '<div class="col-lg-10 col-md-10 col-sm-10 col-xs-10 col-lg-offset-1 col-md-offset-1 col-sm-offset-1 col-xs-offset-1">' +
          '<button type="submit" class="btn btn-primary btn-lg btn-md btn-sm btn-xs btn-chat" id="addcardForm"> Confirm </button>' +
        '</div>' +
      '</div>' +
    '</div>' +
  '</div>';

  return element;
}

$(document).ready(function(){

  var conversation = document.querySelector('#conversations');
  var inputChat = document.querySelector('#inputChat');

  // Initialise websocket
  var socket = io.connect('http://' + document.domain + ':' + location.port);

  socket.on('connect', function() {
		console.log('User has connected!');
	});

  // Initialise watson conversation
  var text = "Hello"

  socket.emit('my event', {data: text});

  // ChatBot response message
  socket.on('my response', function(msg) {
    var text = msg.data;
    var user = msg.user;

    if (msg.intent == "hello") {
      var message = buildMessageRecieve(text);
      conversation.appendChild(message);
      var attachment = buildHelloAttachment();
      conversation.appendChild(attachment);
    } else if (msg.intent == "sign_up") {
      var arr1 = text.split('enter');
      var arr2 = arr1[1].split(".");
      var temp = "<span style='font-weight: 700;'>" + arr2[0] + "</span>";
      var arr2_ = [temp, arr2[1]];
      var arr1_1 = arr2_.join(".");
      var arr1_ = [arr1[0], arr1_1];
      var text = arr1_.join("enter");
      var message = buildMessageRecieve(text);
      conversation.appendChild(message);
    } else if (text.toLowerCase().indexOf("registered!") >= 0) {
      var arr1 = text.toLowerCase().split('registered');
      var text_new1 = [arr1[0], user.firstName];
      var arr1_ = text_new1.join("registered ");
      var text_ = [arr1_, arr1[1]];
      var text = text_.join("");
      var message = buildMessageRecieve(text);
      conversation.appendChild(message);
      var attachment = buildRegisteredAttachment();
      conversation.appendChild(attachment);
    } else if (text.toLowerCase().indexOf("setup complete!") >= 0) {
      var message = buildMessageRecieve(text);
      conversation.appendChild(message);
      var attachment = buildSetupAttachment();
      conversation.appendChild(attachment);
    } else {
      var message = buildMessageRecieve(text);
      conversation.appendChild(message);
    }

    conversation.scrollTop = conversation.scrollHeight;

		console.log('Received message');
	});

  // ChatBot response form
  socket.on('my response', function(msg) {
    var user = msg.user;

    if (msg.form == "signup") {
      var signup = buildSignupForm(user);
      conversation.appendChild(signup);
    }
    if (msg.form == "addcard") {
      var name_arr = [user.firstName, user.lastName];
      var name = name_arr.join(" ")
      var user_arr = [user.bvn, name]
      var addcard = buildCardForm(user_arr);
      conversation.appendChild(addcard);
      var date_input=$('input[name="date"]'); //our date input has the name "date"
      date_input.datepicker({
        format: 'mm/dd/yyyy',
        todayHighlight: true,
        autoclose: true,
      });
    }

    conversation.scrollTop = conversation.scrollHeight;

		console.log('Received message');
	});

  // Button actions

  $('.conversations').on('click', '#getstarted', function() {
    var text = "I want to open account"

    $(this).closest('.attachment').fadeOut();

    //socket.send(text);
    socket.emit('my event', {data: text});

  });

  $('.conversations').on('click', '#setupcard', function() {
    var text = "I want to setup payment card"

    $(this).closest('.attachment').fadeOut();

    //socket.send(text);
    socket.emit('my event', {data: text});

  });

  // Fade out form on confirm

  $('.conversations').on('click', '#signupForm', function() {
    var text = "confirmed"

    $(this).closest('.signupForm').fadeOut();

    //socket.send(text);
    socket.emit('my event', {data: text});

  });

  $('.conversations').on('click', '#addcardForm', function() {
    var text = "confirmed";

    $(this).closest('.addcardForm').fadeOut();

    var card = {
      bvn: inputBVN.value,
      name: inputName.value,
      type: inputType.options[inputType.selectedIndex].value,
      number: inputNumber.value,
      expiry: inputExpiry.value,
      cvc: inputCVC.value
    };

    //socket.send(text);
    socket.emit('my event', {data: text, payment: card});

  });

  // User click to send input
  $("#send").on("click", function(e){
    var text = inputChat.value;
    if (inputChat.value) {
      var message = buildMessageSend(text);
      conversation.appendChild(message);
    }

    socket.emit('my event', {data: text});

    inputChat.value = '';
    conversation.scrollTop = conversation.scrollHeight;

    e.preventDefault();
  });

  //User press enter to send input
  $('#inputChat').keypress(function (e) {
    var key = e.which;
    var text = inputChat.value;

    if(key == 13)  // the enter key code
    {
      if (inputChat.value) {
        var message = buildMessageSend(text);
        conversation.appendChild(message);
      }

      //socket.send(text);
      socket.emit('my event', {data: text});

      inputChat.value = '';
      conversation.scrollTop = conversation.scrollHeight;

      e.preventDefault();
    }
  });

});
