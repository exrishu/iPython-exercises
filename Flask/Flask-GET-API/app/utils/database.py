from .database_connection import DatabaseConnection
import csv

def ReadEmployeeData():
	with DatabaseConnection() as conn:
		cur = conn.cursor()
		cur.execute('select * from employees')
		emp = [{'id': rows[0], 'name': rows[1], 'domain': rows[2], 'role': rows[3]} for rows in cur.fetchall()]
		return emp

def FilterEmloyeeData(id,name,domain,role):
# def FilterEmloyeeData(role):
	with DatabaseConnection() as conn:
		cur = conn.cursor()
		query = "SELECT * FROM employees WHERE"
		to_filter = []
		if id:
			query += ' id= %s AND'
			to_filter.append(id)
		if name:
			query += ' name=%s AND'
			to_filter.append(name)
		if domain:
			query += ' domain=%s AND'
			to_filter.append(domain)
		if role:
			query += ' role=%s AND'
			to_filter.append(role)

		query = query[:-4] + ';'

		cur.execute(query, to_filter)
		results = [{'id': rows[0], 'name': rows[1], 'domain': rows[2], 'role': rows[3]} for rows in cur.fetchall()]
		return results
#
# def InsertEmployeeData():
# 	with open('insert_data.csv', 'r') as f:
# 		reader = csv.reader(f)
# 		next(reader)  # Skip the header row.
# 		for row in reader:
# 			cur.execute(
# 				"INSERT INTO employees VALUES (%s, %s, %s, %s)",
# 				row
# 			)
#
# 	conn.commit()