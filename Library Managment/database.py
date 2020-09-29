import json
book_rec = 'books.json'



def create_new_file():
	with open(book_rec,'w') as file:
		json.dump([],file)

def add_books(name, author):
	books = display_book()
	books.append({'name' : name , 'author' : author, 'read': False})
	_save_all_books(books)



def display_book():
	with open(book_rec, 'r') as file:
		return json.load(file)


def _save_all_books(books):
	with open(book_rec, 'w') as file:
		json.dump(books,file)

def read_book_true(name):
	books = display_book()
	for book in books:
		if name in book['name']:
			book['read'] = True

	_save_all_books(books)




def delete_book(name):
	books = display_book()
	books = [book for book in books if name != book['name']]
	_save_all_books(books)
