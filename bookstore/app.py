books = []
file_name = "book_list"
from utils.storage import *

#menu
USER_CHOICE = """
Enter:
- 'a' to add a new book
- 'd' to list all books
- 'm' to mark a book as read
- 'r' to remove a book
- 'q' to quit
- 's' to save list to a file
- 'l' load list from file

Your choice:
"""


def populate_library() -> None:
    add_book('AI aesthetics', 'Lev Manovich', books)
    add_book('1984', 'George Orwell', books)

def prompt_add_book() -> None:
    name = input("Please introduce the name of the book:\n")
    author = input("Please introduce the author of the book:\n")
    add_book(name, author, books)

def prompt_read_book() -> None:
    name = input("Please introduce the name of the book that you'd like to mark as read:\n")
    mark_book_as_read(name, books)

def prompt_delete_book() -> None:
    name = input("Please introduce the name of the book that you'd like to delete:\n")
    delete_book(name, books)


def menu() -> None:
    while True:
        try:
            user_input = input(USER_CHOICE)
            if user_input == 'a': #ask for book name and author
                prompt_add_book()
            elif user_input == 'd': #show all the books in our list
                list_books()
            elif user_input == 'm': #ask for book name and change it to "read" in our list
                prompt_read_book()
            elif user_input == 'r': #ask for book name and remove book from list
                prompt_delete_book()
            elif user_input == 's':  # safe list of books into file
                save_list_books_to_csv_file(file_name)
            elif user_input == 'l':  # safe list of books into file
                load_list_of_books_from_csv_file(file_name)
            elif user_input == 'q':
                print("bye")
                exit()
            else:
                print("Incorrect option")
        except KeyboardInterrupt:
            print('bye')
            exit()


populate_library()
menu()



