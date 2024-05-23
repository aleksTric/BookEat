
class User:
    def __init__(self, canvas, db, text_item_user):
        self.canvas = canvas 
        self.db = db
        self.text_item_user = text_item_user
    
    def is_user(self):
      username = self.canvas.itemcget(self.text_item_user, 'text')
      print(f"{username}")
      query = "SELECT email FROM account WHERE username LIKE %s "
      cursor = self.db.execute_query(query, ('%' + username + '%',))
      info = cursor.fetchall()
      email = info
      print(f"{email}")
    #def get_user():
       #