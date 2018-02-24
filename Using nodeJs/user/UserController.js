var express = require('express');
var router = express.Router();
var bodyParser = require('body-parser');
router.use(bodyParser.urlencoded({ extended: true}));
router.use(bodyParser.json());

var User = require('./User');
module.exports = router;


//added to make a rest api
//creates a new user
router.post('/', function(req, res){

	User.create({
			name : req.body.name,
			email : req.body.email,
			password : req.body.password
		},
		function (err, user) {
			if (err) return res.status(500).send("There was a problem adding the information to the database.");
			res.status(200).send(user);
		});
});

	//Returns all the users in the database

router.get('/', function(req, res){
	User.find({}, function (err, users){
		if (err) return res.status(500).send("There was a problem finding the users.");
		res.status(200).send(users);

	});
});

module.exports = router;

//gets a single user from database

router.get('/:id', function (req, res){
	User.findById(req.params.id, function(err, user){
		if (err) return res.status(500).send("There was a problem finding the user.");
		if(!user) return res.status(404).send("No user found.");
		res.status(200).send(user);


	});
});

//delete user from database

router.delete('/:id', function (req, res){

	User.findByIdAndRemove(req.params.id, function(err, user){
		if (err) return res.status(500).send("There was a problem deleting the user.");
		res.status(200).send("User "+ user.name + "was deleted.");


	});
});


//updtaes single user in database
router.put('/:id', function(req, res){
	
	User.findByIdAndUpdate(req.params.id, req.body, {new: true}, function(err, user){
		if (err) return re.status(500).send("There was a problem updating the user.");
		res.status(200).send(user);


	});
});
//A good practice when updating some values is to request the updated value to be sent back to you. This is important as you want to have access to the newly updated value. Hence, you add another, fourth parameter {new:true} which stands for the option of which version of the value, in your case the user, you want to return. The one before the update, or the one after. Returning this value will show you the user you updated.
//The server is listening for an HTTP request to hit the route '/:id' with a GET method. When such a request occurs, the callback function will be called. Everything inside this function will be evaluated and executed.