//server.js
var app = require('./app');
var port = process.env.PORT || 3000;

var server = app.listen(port, function(){
	console.log('Express server listening on port' + port);
});// this line creates server
// This app is the actual app object you created in app.js
