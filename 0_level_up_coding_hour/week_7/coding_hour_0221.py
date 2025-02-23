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
        print(f"{book.title} has been added from {self.name}'s inventory.")

    def remove_book(self, book_title):
        for book in self.book_inventory:
            if book.title is book_title:
                self.book_inventory.remove(book)
                self.total_books -= 1
                print(f"{book_title} has been removed from {self.name}'s inventory.")

    def borrow_book(self, book_title, borrower_name):
        for book in self.book_inventory:
            if book.title is book_title and book.is_borrowed:
                print(f"{book.title} is currently checked out to {book.borrower_name}.")
            elif book.title is book_title:
                book.is_borrowed = True
                book.borrower_name = borrower_name
                print(f"{borrower_name} has checked out {book_title}.")

    def return_book(self, book_title, borrower_name):
        for book in self.book_inventory:
            if book.title is book_title and book.is_borrowed:
                book.is_borrowed = False
                book.borrower_name = None
                print(f"{borrower_name} has returned {book_title}.")

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
library = Library("Madison Public Library")
print(library)

book_1 = Book("The Catcher in the Rye", "J. D. Salinger")
#print(f"BOOK 1\n{book_1}")
library.add_book_to_inventory(book_1)

book_2 = Book("Great Expectations", "Charles Dickens")
#print(f"BOOK 2\n{book_2}")
library.add_book_to_inventory(book_2)

book_3 = Book("War and Peace", "Leo Tolstoy")
#print(f"BOOK 3\n{book_3}")
library.add_book_to_inventory(book_3)

print(library)
# library.remove_book(book_2)
# print(library)
library.borrow_book("Great Expectations", "Robert Young")
print("")
print(library)
library.borrow_book("Great Expectations", "Robert Young")
library.return_book("Great Expectations", "Robert Young")
print("")
print(library)

library.remove_book("The Catcher in the Rye")
print("")
print(library)