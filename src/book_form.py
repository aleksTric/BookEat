from book import Books
import tkinter.messagebox
import mysql.connector
from categories import Categories
import json

class Book_Form(Books): 
    def __init__(self):
      pass

    def check_book(self,title,category,author,date):
      book_obj = Books(title,category,author,date)
      title =book_obj.get_title()
      category =book_obj.get_categ()
      author =book_obj.get_author()
      date=book_obj.get_date()

      
      if Books.get_book(title):
         tkinter.messagebox.showerror("Error", "the book already exists")
      else:
           if Categories.get_category_id(category) :
            id = Categories.get_category_id(category)
            print(id)
            self.insert_book(title,id,author,date)
           else:
            tkinter.messagebox.showerror("Error", "the category doesnt exist") 
    
    def insert_book(self,title,category_id,author,date):
      try: 
        
          conn = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="bookeat"
          )
         
          cursor = conn.cursor()
      
          sql = "INSERT INTO books (title, cat_id, author, date) VALUES (%s, %s, %s, %s)"
          cursor.execute(sql, (title, category_id, author, date))
          conn.commit()
          
      except mysql.connector.Error as error:
            print("Failed to insert book:", error)   
      finally:
            
            if conn.is_connected():
                cursor.close()
                conn.close()
    
    
    
    
    def check_category(self,category):
      categ_obj = Categories(category)
      category =categ_obj.get_category_name()
      if Categories.get_category(category):
         tkinter.messagebox.showerror("Error", "the category already exists")
      else:
        
         self.insert_category(category)
         
    def insert_category(self,category):
      try: 
        
          conn = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="bookeat"
          )
         
          cursor = conn.cursor()
          print("Category to insert: ", category)
          sql = "INSERT INTO categories (category_name) VALUES (%s)"
          cursor.execute(sql, (category,))
      
          conn.commit()
          
      except  mysql.connector.Error as error:
             print("Failed to insert category:", error)   
      finally:
            
            if conn.is_connected():
                cursor.close()
                conn.close()

    def show_message(self):
       pass
    
    def check_json(self,path):
      try:
        # Load the JSON file
        with open(path, 'r') as file:
            data = json.load(file)
            print(data)
        
        if 'books' not in data:
            raise ValueError("JSON does not contain 'books' key")
        
        
        if not isinstance(data['books'], list):
            raise ValueError("'books' should be a list")
        
        
        required_attributes = {'title', 'category', 'author', 'date'}
        
        # Validate each book entry
        for book in data['books']:
            
            if not isinstance(book, dict):
                raise ValueError(f"Each book entry should be a dictionary. Found: {type(book)}")
            
            
            missing_attributes = required_attributes - book.keys()
            if missing_attributes:
                raise ValueError(f"Book entry missing attributes: {missing_attributes}")
            
            self.check_book(book['title'],book['category'],book['author'],book['date'])
            
        
        print("JSON file is valid.")
      except json.JSONDecodeError as e:
        print(f"Invalid JSON file: {e}")
      except Exception as e:
        print(f"Error: {e}")