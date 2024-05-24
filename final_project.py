# Library Catalog 

class book:
    def __init__(self, title, genre, isbn, quantity):
        self.title = title
        self.genre = genre
        self.isbn = isbn
        self.quantity = quantity

    #### display book details
    def display_book_detail(self):                 
        print(f"Book Title : {self.title}")
        print(f"Genre : {self.genre}")
        print(f"ISBN : {self.isbn}")
        print(f"Quantity : {self.quantity}")


class LibraryCatalog:

    ### create dict 
    isbn = {"978-0-434-09800-2": "A Clockwork Orange"}
    
    #### add a book function
    def add_book():
        isbn = {"978-0-434-09800-2": "A Clockwork Orange"}
        isbn.update({"0060188707": "Don Quixote"})
        print(isbn)
       
    ### remove book from the catalog
    def remove_book():
        isbn = {"978-0-434-09800-2": "A Clockwork Orange", "0060188707": "Don Quixote"} 
        del isbn['0060188707']
        print(isbn)


    #### search book by Title, Genre, Author 
    def search():
         isbn = {"978-0-434-09800-2": "A Clockwork Orange", "0060188707": "Don Quixote"}

    ####choose menu
    def choose_func():
        menu = "1) Add a Book\n2) Remove a Book\n3) Search a Book\n4) Display all Book\n5) Exit the program!"
        print(menu)
        choose = input("choose an option: ")
         
   


library = book("A Clockwork Orange", "Novel", "978-0-434-09800-2", 15)
library.display_book_detail()
obc = LibraryCatalog
print(LibraryCatalog.isbn)
LibraryCatalog.add_book()
LibraryCatalog.remove_book()
LibraryCatalog.search()
LibraryCatalog.choose_func()