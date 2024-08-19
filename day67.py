# Library Management System using Python
class Library:
  def __init__(self):
    self.no_of_books = 0
    self.books = []
    
  def add_book(self,book):
    self.books.append(book)
    self.no_of_books = len(self.books)
  
  def showInfo(self):
    print(f"Number of books in the library is {self.no_of_books}")
    for book in self.books:
      print(book)

l1 = Library()
l1.add_book("Book1")
l1.add_book("Book2")
l1.add_book("Book3")
l1.showInfo()
