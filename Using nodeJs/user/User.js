//user.js
var mongoose = require('mongoose');
var UserSchema = new mongoose.Schema({
	name: String,
	email: String,
	password: String
});

mongoose.model('User', UserSchema);
module.exports = mongoose.model('User');
//By specifying mongoose.model('User', UserSchema) you’re binding the layout of the schema to the model which is named 'User' .