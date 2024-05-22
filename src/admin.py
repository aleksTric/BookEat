from book_form import Book_Form
from library_form import Library_Form

class Admin:
    def __init__(self):
     self.book_form = Book_Form()
     self.library_form = Library_Form()

    def add_book(self,title,category,author,date):
     self.book_form.check_book(title,category,author,date)
    
    def add_category(self,category):
     self.book_form.check_category(category)

    def upload_json(self,path):
      self.book_form.check_json(path)

    def search_bycateg(self,categ):
       
       books =self.library_form.get_books(categ)
       return books