## Developing context Manager
import psycopg2


class DatabaseConnection:
	def __init__(self):
		self.connection = None
		self.dsn = "dbname=database_name user=user_name password=db_password host=hostname port=5432"

	def __enter__(self):
		self.connection = psycopg2.connect(self.dsn)
		return self.connection

	def __exit__(self, exc_type, exc_val, exc_tb):
		self.connection.commit()
		self.connection.close()
