from typing import List
"""
Storing and retrieving books from a list.
"""

#Adds book to the list
def add_book(name: str, author: str, books: List) -> None:
    try:
        books.append({'name': name, 'author': author, 'read': False})
    except TypeError:
        print("It was not possible to add the book")
    except ValueError:
        print("It was not possible to add the book")
    else:
        print(f"Book {name} added to the library")

#Try to find the book in the list and it marks it as read
def mark_book_as_read(name: str, books: List) -> None:
    for book in books:
        if book['name'] == name:
            try:
                book['read'] = True
                print(f" {name} was marked as read")
                break
            except TypeError:
                print(f" There was a problem marking the book {name} as read.")
            except ValueError:
                print(f" There was a problem marking the book {name} as read.")
    else:
        print(f"Error: {name} was not found in the library")

#It deletes the book if it's in the list
def delete_book(name: str, books: List) -> None:
    for i in range(len(books)):
        if books[i]['name'] == name:
            print(name)
            try:
                del books[i]
                print(f"The book {name} was deleted from the library")
                return
            except IndexError:
                print(f" There was a problem deleting the book {name} from the library.")

    print(f"Error: {name} was not found in the library")

#It prints all the books in the list
def list_books(books: List) -> None:
    for book in books:
        read_str = ""
        try:
            if book["read"] == True:
                read_str = "You have already read this book."
            else:
                read_str = "You haven't read this book yet."
        except TypeError:
            print(f" There was a problem accessing the list of books.")
        except ValueError:
            print(f" There was a problem accessing the list of books.")

        print(f'{book["name"]} written by {book["author"]}. {read_str}')

#It loads the books from the csv file into the list
def load_list_of_books_from_csv_file(file_name: str, books: List) -> None:
    books.clear()
    lines = ()
    with open(file_name+".csv", 'r') as file:
        for line in file.readlines():
            new = line.strip().split(',')
            add_book(new[0], new[1])
            if new[1] == 'True':
                mark_book_as_read(new[2])

#It saves the list of books to a csv file
def save_list_books_to_csv_file(file_name: str, books: List) -> None:
    with open(file_name+".csv", 'w') as file:  # opening the file for writing
        for book in books:
            file.write(f'{book["name"]},{book["author"]},{book["read"]}\n')


