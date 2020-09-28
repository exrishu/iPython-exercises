import udemy.milestone_2.database as database

user = '''
Enter the User's choice:
	A - Add new book
	L - List all the books
	R - To mark book as read
	D - Delete the book
	Q - Quit the application 
		  
	Please enter which action you want to perform : '''


def menu():
	choice = input(user)
	while choice.lower() != 'q':
		if choice.lower() == 'a':
			prompt_add_book()
		elif choice.lower() == 'l':
			list_book()
		elif choice.lower() == 'r':
			prompt_read_book()
		elif choice.lower() == 'd':
			prompt_delete_book()
		choice = input(user)


def prompt_add_book():
	book_name = input('Enter the book name: ')
	author = input('Enter the author name: ')

	database.add_books(book_name, author)


def list_book():
	books = database.display_book()
	i = 0
	for book in books:
		i = i + 1
		read = 'YES' if book['read'] == '1' else 'NO'
		print(f" {i} - \n Book Name : {book['name']},\nAuthor :{book['author']},\nRead:{read} \n\n")


def prompt_read_book():
	list_book()
	book_name = input('Enter the book name from above list which you want to mark as read: ')

	database.read_book_true(book_name)


def prompt_delete_book():
	list_book()
	book_name = input('Enter the book name from above list which you want remove from your library: ')

	database.delete_book(book_name)
	print(
		f"The book '{book_name}' has been successfully removed from your library.\n These are the books remaining in your Library.")
	list_book()


menu()
