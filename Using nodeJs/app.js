//app.js
var express = require('express');
var app = express();
var db = require('./db');//added after db.js
module.exports = app;
//This file will be used for configuring the app
//We use module.exports to make this app object visible to the rest of the program when we call for it using require()
//By specifying it like this, we are telling require to grab a file in the same directory where app.js is located and include it. That’s it. Now our app knows it has a database ready and waiting to be accessed.

//addded after UserController.js
var UserController = require('./user/UserController');
app.use('/users', UserController);

module.exports = app;

// notes for postman
//Switch to the body tab, and enter key — value pairs matching the user model you created earlier. You need a name, an email and a password. Hit send. Voilá! A response. If everything went fine, the response will contain data matching the recently created user.
//Now, go ahead and change the HTTP method to GET, and hit send once again. You’ll see all the created users get returned from the database. Go ahead and play around a bit with this, add some more users, and watch how the GET request behaves.
