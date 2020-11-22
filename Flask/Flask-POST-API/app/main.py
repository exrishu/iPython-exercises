import flask
from flask import request, jsonify, abort
from flask_cors import CORS

from .utils.database import insert_lead

app = flask.Flask(__name__)
CORS(app)
cors = CORS(app, resources={
	r"/*": {
		"origins": "*"
	}
})

@app.route('/', methods=['GET'])
def home():
	return "<h1>Employee Data</h1>"


@app.route('/api/v1/post/data/', methods=['POST'])
def create_entry():
	if not request.json or not 'name' in request.json or not 'mobile' in request.json:
		abort(400)

	task = {
		'name': request.json['name'],
		'mobile': request.json['mobile'],
		'email': request.json['email'],
		'service': request.json['service'],
		'description': request.json['description']
	}
	insert_lead(task['name'], task['mobile'], task['email'], task['service'], task['description'])

	return jsonify({'status': 'Request Processed Successfully'}), 201
