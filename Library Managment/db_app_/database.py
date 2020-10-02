from udemy.milestone_2.database_connection import DatabaseConnection


def create_new_file():
	with DatabaseConnection('data.db') as connection:
		cursor = connection.cursor()
		cursor.execute('CREATE TABLE IF NOT EXISTS books(name text primary key ,author text,read integer)')


def add_books(name, author):
	with DatabaseConnection('data.db') as connection:
		cursor = connection.cursor()
		cursor.execute('INSERT INTO BOOKS VALUES (?,?,0)', (name, author))


def display_book():
	with DatabaseConnection('data.db') as connection:
		cursor = connection.cursor()
		cursor.execute('SELECT * FROM books')
		books = [{'name': rows[0], 'author': rows[1], 'read': rows[2]} for rows in cursor.fetchall()]
		return books


def read_book_true(name):
	with DatabaseConnection('data.db') as connection:
		cursor = connection.cursor()
		cursor.execute('UPDATE books SET read=1 where name =?', (name,))


def delete_book(name):
	with DatabaseConnection('data.db') as connection:
		cursor = connection.cursor()
		cursor.execute('DELETE FROM books where name =?', (name,))
