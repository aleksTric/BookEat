from book_form import Book_Form

class Admin:
    def __init__(self):
     self.book_form = Book_Form()
     
    def add_book(self,title,category,author,date):
     self.book_form.check_book(title,category,author,date)
    
    def add_category(self,category):
     self.book_form.check_category(category)

    def upload_json(self):
      pass