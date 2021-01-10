from bookstore.utils.storage import *
from tests.bookstore.conftest import *
from typing import List

#Adds book to the list
def test_add_book() -> None:
    books = []
    title, author = load_book_title_author()
    add_book(title, author, books)
    found = False
    print(len(books))
    for i in range(len(books)):
        if books[i]['name'] == title and books[i]['author'] == author:
            books.clear()
            found = True
    if found:
        assert True
    else:
        assert False

#It deletes the book if it's in the list
def test_delete_book() -> None:
    books = []
    title, author = load_book_title_author()
    add_book(title, author, books)
    delete_book(title, books)
    found = False
    for i in range(len(books)):
        if books[i]['name'] == title and books[i]['author'] == author:
            found = True
    books.clear()
    if found:
        assert False
    else:
        assert True

def test_save_list_books_to_csv_file() -> None:
    books = load_test_data()
    file_name = "test_books.csv"
    save_list_books_to_csv_file(file_name, books)
    counter = 0
    with open(file_name+".csv", 'r') as file:
        for line in file.readlines():
            new = line.strip().split(',')
            if new[0] != books[counter]['name'] or new[1] != books[counter]['author'] or new[2] != books[counter]['read']:
                assert False
            counter = counter + 1
    assert True


#Try to find the book in the list and it marks it as read
def test_mark_book_as_read() -> None:
    books = load_non_read_test_data()
    mark_book_as_read(books[0]['name'], books)
    assert books[0]['read'] == True
