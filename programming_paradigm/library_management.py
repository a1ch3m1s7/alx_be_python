class Book:
	def __init__(self, title, author):
		self._is_checked_out = False
		self.title = title
		self.author = author

	def check_out(self):
		if not self._is_checked_out:
			self._is_checked_out = True
			return True
		return False

	def return_book(self):
		if self._is_checked_out:
			self._is_checked_out = False
			return True
		return False

	def is_available(self):
		return not self._is_checked_out



class Library:
	def __init__(self):
		self._books = []

	def add_book(self, book):
		self._books.append(book)

	def check_out_book(self, title):
		for book in self._books:
			if book.title == title and book.is_available():
				book.check_out()
				return
		print(f"'{title}' is not available or doesn't exist.")

	def return_book(self, title):
		for book in self._books:
			if book.title == title and not book.is_available():
				book.return_book()
				return
		print(f"'{title}' is not checked out or doesn't exist.")


	def list_available_books(self):
		available = [book for book in self._books if book.is_available()]
		if not available:
			print("No _books available.")
		else:
			for book in available:
				print(f"- {book.title} by {book.author}")