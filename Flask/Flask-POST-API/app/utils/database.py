from .database_connection import DatabaseConnection

def insert_lead(name, mobile, email, services, description):
	with DatabaseConnection() as conn:
		cur = conn.cursor()

		insert_query = '''INSERT INTO rwc_leads_data(id,name,mobile,email,services,description,crtd_on) values(nextval(%s),%s,%s,%s,%s,%s,%s)'''
		records_insert = ('s_no', name, mobile, email, services, description, 'now()')
		cur.execute(insert_query, records_insert)

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
