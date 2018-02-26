from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
import uuid
import jwt
import datetime
from functools import wraps

app = Flask(__name__)

#file_path = os.path.abspath(os.getcwd())+"/todo.db"
#print(file_path)
app.config['SECRET_KEY'] = 'thisissecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/Shivani Singh/New folder (3)/web-API/Using Flask framework/todo.db'
#C:\Users\Shivani Singh\Documents\webApiEg
db = SQLAlchemy(app)

class User(db.Model):
	id = db.Column(db.Integer, primary_key = True )
	public_id = db.Column(db.String(50), unique = True)
	name = db.Column(db.String(50))
	password = db.Column(db.String(80))
	#admin = db.Colummn(db.Boolean)

class Todo(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	text = db.Column(db.String(50))
	complete = db.Column(db.Boolean)
	user_id = db.Column(db.Integer)


def tokenRequired(f):
	@wraps(f)
	def decorated(*args, *kwargs)



#########
@app.route('/user', methods = ['GET'])
def getUsers():
	users = User.query.all()
	output = []

	for user in users:
		user_data = {}
		user_data['public_id'] = user.public_id
		user_data['name'] = user.name
		user_data['password'] = user.password
		output.append(user_data)
	return jsonify({'users': output})

@app.route('/user/<public_id>', methods = ['GET'])
def getOneUser(public_id):
	
	user = User.query.filter_by(public_id = public_id).first()

	if not user:
		return jsonify({'message': 'No such user found'})
	
	data_user = {}
	data_user['public_id'] = user.public_id
	data_user['name'] = user.name
	data_user['password'] = user.password

	return jsonify({'user': data_user})

@app.route('/user/<public_id>', methods = ['DELETE'])
def deleteUser(public_id):

	user = User.query.filter_by(public_id = public_id).first()

	if not user:
		return jsonify({'message': 'No such user found'})
	
	db.session.delete(user)
	db.session.commit()

	return jsonify({'message': 'deleted'})

@app.route('/user', methods = ['POST'])
def addUser():
	data = request.get_json()
	newUser = User(public_id = str(uuid.uuid4()), name  = data['name'], password = data['password'])
	db.session.add(newUser)
	db.session.commit()
	return jsonify({'message': 'New user added'})

@app.route('/user/<public_id>', methods = ['PUT'])
def updateUser(public_id):
	user = User.query.filter_by(public_id = public_id).first()
	if not user:
		return jsonify({'message': 'No such user found'})
	
	user.name = "BabyCal"
	db.session.commit()

	return jsonify({'message': 'Name changed'})


@app.route('/login')
def login():
	auth = request.authorization

	if not auth or not auth.username or not auth.password:
		return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm = "login required!"'})

	user = User.query.filter_by(name = auth.username).first()

	if not user:
		return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm = "login required!"'})

	if user.password == auth.password :
		token = jwt.encode({'public_id': user.public_id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes = 30)}, app.config['SECRET_KEY'])

		return jsonify({'token': token.decode('UTF-8')})

	return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm = "login required!"'})



if __name__ == '__main__':
	app.run(debug = True)

