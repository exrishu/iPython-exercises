## Developing context Manager
import psycopg2


class DatabaseConnection:
	def __init__(self):
		self.connection = None
		self.dsn = "dbname=da609iukq3i5lj user=ukzbxlqpyruezw password=71c453ee142b50195819d4b8df51c9bf4b8e1bc61c19e826a1a98502384694a8 host=ec2-3-224-97-209.compute-1.amazonaws.com port=5432"


	def __enter__(self):
		self.connection = psycopg2.connect(self.dsn)
		return self.connection

	def __exit__(self, exc_type, exc_val, exc_tb):
		self.connection.commit()
		self.connection.close()


