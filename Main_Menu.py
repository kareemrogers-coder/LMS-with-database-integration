from authors_add import add_authors
from authors_delete import delete_authors
from authors_fetch import fetch_all_authors
from authors_fetch import author_search

from books_add import add_books
from books_delete import delete_books
from books_fetch import fetch_all_books
from books_fetch import book_search

from users_add import add_users
from users_delete import delete_users
from users_fetch import fetch_all_users
from users_fetch import user_search


from borrow_book import borrow_books
from return_books import return_books

def library_menu():
    while True:
        action = input('''
Welcome to the Library Management System!

        Main Menu:
        1. Book Operations
        2. User Operations
        3. Author Operations
        4. Quit
 ''') 
        if action == "1":
            book_operations()
            
        elif action == "2":
            user_operations()
            
        elif action == "3":
            author_operations()
            
        elif action == "4":
            print("Exiting program")
            break
        else:
            print("Invalid entry, please try again.")


def book_operations():
        while True:
            print("\nBook Operations:")
            print("1. Add a new book")
            print("2. Borrow a book") 
            print("3. Return a book") 
            print("4. Search for a book")
            print("5. Display all books")
            print("6. Back to Main Menu")
            action = input("Enter your choice: ")

            if action == '1':
                add_books()
            elif action == '2':
                borrow_books()
                
            elif action == '3':
                return_books()
              
            elif action == '4':
                book_search()

            elif action == '5':
                fetch_all_books()
               
            elif action == '6':
                break
            else:
                print("Invalid entry, please try again.")


def user_operations():
        while True:
            print("\nUser Operations:")
            print("1. Add a new user")
            print("2. View user details")
            print("3. Display all users")
            print("4. Back to Main Menu")
            choice = input("Enter your choice: ")

            if choice == '1':
                add_users()
            elif choice == '2':
                user_search()
            elif choice == '3':
                fetch_all_users()
            elif choice == '4':
                break
            else:
                print("Invalid entry, please try again.")



def author_operations():
        while True:
            print("\nAuthor Operations:")
            print("1. Add a new author")
            print("2. View author details")
            print("3. Display all authors")
            print("4. Back to Main Menu")
            choice = input("Enter your choice: ")

            if choice == '1':
                add_authors()
            elif choice == '2':
                author_search()
            elif choice == '3':
                fetch_all_authors()
            elif choice == '4':
                break
            else:
                print("Invalid entry, please try again.")

library_menu()
