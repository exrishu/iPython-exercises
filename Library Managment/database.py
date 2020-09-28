book_rec = 'books.txt'


def add_books(name, author):
	with open(book_rec, 'a') as file:
		file.write(f"{name},{author},0\n")


def display_book():
	with open(book_rec, 'r') as file:
		books = [line.strip().split(',') for line in file.readlines()]

	books = [{
		'name': book[0],
		'author': book[1],
		'read': book[2]}
		for book in books
	]
	return books


def read_book_true(name):
	books = display_book()
	for book in books:
		if name in book['name']:
			book['read'] = '1'

	_save_all_books(books)


def _save_all_books(books):
	with open(book_rec, 'w') as file:
		for book in books:
			file.write(f"{book['name']},{book['author']},{book['read']}\n")


def delete_book(name):
	books = display_book()
	books = [book for book in books if name != book['name']]
	_save_all_books(books)
