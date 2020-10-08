## Developing context Manager
import psycopg2


class DatabaseConnection:
	def __init__(self):
		self.connection = None
		self.dsn = "dbname=databse_name user=user_id password=db_passwrd host=host port=5432"


	def __enter__(self):
		self.connection = psycopg2.connect(self.dsn)
		return self.connection

	def __exit__(self, exc_type, exc_val, exc_tb):
		self.connection.commit()
		self.connection.close()


