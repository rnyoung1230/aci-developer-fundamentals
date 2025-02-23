# CODING HOUR - 02/21

# Library Management System
'''
Create a library management system that tracks books and their borrowing.
You'll need to implement two classes: Book and Library.

Create a Book class with these attributes:
- title
- author
- isbn
- is_borrowed (defaults to False)
- borrower_name (defaults to None)
'''

import random

class Library:
    # class variables and methods

    # instance variables and methods
    def __init__(self, name):
        self.name = name
        self.book_inventory = []
        self.total_books = 0

    def __str__(self):
        book_inventory_display = ''

        if len(self.book_inventory) > 0:
            for book in self.book_inventory:
                book_inventory_display += f"{str(book)}\n"

        return f"\nLibrary Name: {self.name}\n" \
               f"\nBook Inventory ({self.total_books} books):\n{book_inventory_display}\n"

    def add_book_to_inventory(self, book):
        self.book_inventory.append(book)
        self.total_books += 1
        return f"{book.title} has been added from {self.name}'s inventory."

    def remove_book(self, book_title):
        message = f"{book_title} was not found."

        for book in self.book_inventory:
            if book.title is book_title:
                self.book_inventory.remove(book)
                self.total_books -= 1
                message = f"{book_title} has been removed from {self.name}'s inventory."

        return message

    def borrow_book(self, book_title, borrower_name):
        message = f"{book_title} was not found."

        for book in self.book_inventory:
            if book.title is book_title:
                if book.is_borrowed:
                    message = f"{book.title} is currently checked out to {book.borrower_name}."
                else:
                    book.is_borrowed = True
                    book.borrower_name = borrower_name
                    message =  f"{borrower_name} has checked out {book_title}."

        return message

    def return_book(self, book_title, borrower_name):
        message = f"{book_title} was not found."

        for book in self.book_inventory:
            if book.title is book_title and book.is_borrowed:
                book.is_borrowed = False
                book.borrower_name = None
                message = f"{borrower_name} has returned {book_title}."

        return message

class Book:
    # class variables and methods
    isbns = []

    @classmethod
    def get_isbn(cls):
        # Generate a candidate 10-digit number to use
        isbn = random.randint(1000000000, 9999999999)

        # Verify number isn't already assigned, keep generating numbers until you find one that's available
        while isbn in cls.isbns:
            isbn = random.randint(1000000000, 9999999999)

        # Add the number to the list of assigned accounts
        cls.isbns.append(isbn)

        return isbn

    def __init__(self, title, author):
        self.title = title
        self.author = author
        #ISBN is an acronym that stands for International Standard Book Number.This is a 10-digit number assigned to all
        # books and book-like publications that are published internationally.
        self.isbn = Book.get_isbn()
        self.is_borrowed = False
        self.borrower_name = None

    def __str__(self):
        return f"Title: {self.title}\n" \
               f"Author: {self.author}\n" \
               f"ISBN: {self.isbn}\n" \
               f"Is Borrowed: {self.is_borrowed}\n" \
               f"Borrower Name: {self.borrower_name}\n"

#################################### TEST CODE ########################################
# Create a library object
library = Library("Madison Public Library")
print(library)

# Create some book objects and add to the library object's inventory
# Print the return message confirming the add was successful
book_1 = Book("The Catcher in the Rye", "J. D. Salinger")
#print(f"BOOK 1\n{book_1}")
print(library.add_book_to_inventory(book_1))

book_2 = Book("Great Expectations", "Charles Dickens")
#print(f"BOOK 2\n{book_2}")
print(library.add_book_to_inventory(book_2))

book_3 = Book("War and Peace", "Leo Tolstoy")
#print(f"BOOK 3\n{book_3}")
print(library.add_book_to_inventory(book_3))

# Print details of library object showing the added books and total inventory count
print(library)

# Test borrow_book function and print library object showing the updated borrower and is_borrowed fields
print(library.borrow_book("Great Expectations", "Robert Young"))
print("")
print(library)

# Test borrow_book function for when a book is already checked out
print(library.borrow_book("Great Expectations", "Robert Young"))

# Test return_book function and print library object showing the updated borrower and is_borrowed fields
print(library.return_book("Great Expectations", "Robert Young"))
print("")
print(library)

# Test the remove_book function and confirm successful message is printed
print(library.remove_book("The Catcher in the Rye"))
print("")
# Print the library object showing the removed book is no longer displayed as part of inventory
print(library)

# Test removing and borrowing a book that isn't in the library's inventory...should get a not found message
print(library.remove_book("The Great Gatsby"))
print(library.borrow_book("The Odyssey", "Tim Gies"))