class User:
    def __init__(self, name, library_id):
        self._name = name
        self._library_id = library_id
        self._borrowed_books = []

    # Getters and setters
    def get_name(self):
        return self._name
  
    def get_borrowed_books(self):
        return self._borrowed_books
    
    def borrow_book(self, book):
        if book.is_available():
            self._borrowed_books.append(book)
            book._available = False
        else:
            print("Sorry, this book is not available for borrowing.")

    def return_book(self, book):
        if book in self._borrowed_books:
            self._borrowed_books.remove(book)
            book._available = True
        else:
            print("You haven't borrowed this book.")

    def __str__(self):
        borrowed_titles = ", ".join([book.get_title() for book in self._borrowed_books])
        return f"Name: {self._name}\nLibrary ID: {self._library_id}\nBorrowed Books: {borrowed_titles}"
"play_circleeditcontent_copy"
"author.py" & "genre.py"

class Author:
    # ... 

 class Genre : ()