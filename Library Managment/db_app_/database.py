import json
import sqlite3

book_rec = 'books.json'


def create_new_file():
	connection = sqlite3.connect('data.db')
	cursor = connection.cursor()

	cursor.execute('CREATE TABLE IF NOT EXISTS books(name text primary key ,author text,read integer)')
	connection.commit()
	connection.close()


def add_books(name, author):
	connection = sqlite3.connect('data.db')
	cursor = connection.cursor()
	cursor.execute('INSERT INTO BOOKS VALUES (?,?,0)', (name, author))
	connection.commit()
	connection.close()


def display_book():
	connection = sqlite3.connect('data.db')
	cursor = connection.cursor()
	cursor.execute('SELECT * FROM books')
	books = [{'name': rows[0], 'author': rows[1], 'read': rows[2]} for rows in cursor.fetchall()]
	connection.close()

	return books


def _save_all_books(books):
	with open(book_rec, 'w') as file:
		json.dump(books, file)


def read_book_true(name):
	connection = sqlite3.connect('data.db')
	cursor = connection.cursor()
	cursor.execute('UPDATE books SET read=1 where name =?', (name,))
	connection.commit()
	connection.close()


def delete_book(name):
	connection = sqlite3.connect('data.db')
	cursor = connection.cursor()
	cursor.execute('DELETE FROM books where name =?', (name,))
	connection.commit()
	connection.close()
