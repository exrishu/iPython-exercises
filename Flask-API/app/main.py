from .utils.database import ReadEmployeeData,FilterEmloyeeData
import flask
from flask import request, jsonify


app = flask.Flask(__name__)


@app.route('/', methods=['GET'])
def home():
	return "<h1>Employee Data</h1>"


@app.route('/api/v1/resources/employee/all', methods=['GET'])
def api_all():
	emplyee_data = ReadEmployeeData()
	return jsonify(emplyee_data)


@app.route('/api/v1/resources/employee', methods=['GET'])
def api_filter():

	query_param = request.args

	id = query_param.get('id')
	name = query_param.get('name')
	domain = query_param.get('domain')
	role = query_param.get('role')

	emp_filter_data = FilterEmloyeeData(id,name,domain,role)

	return jsonify(emp_filter_data)
