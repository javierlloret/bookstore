
#It loads the csv file with the data
def load_test_data():
    books = [
        { 'name': 'mybookname', 'author': 'myauthorname', 'read': 'False'},
        { 'name': 'myotherbook', 'author': 'myauthorname2', 'read': 'True'}
    ]
    return books


def load_non_read_test_data():
    books = [
        { 'name': 'mybookname', 'author': 'myauthorname', 'read': 'False'},
        { 'name': 'myotherbook', 'author': 'myauthorname2', 'read': 'False'}
    ]
    return books

def load_book_title_author():
    title = "another title"
    author = "you"
    return title, author

