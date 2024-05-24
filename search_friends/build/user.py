
class User:
    def __init__(self, canvas, db):
        self.canvas = canvas 
        self.db = db
    
    def is_user(self, text_item_user):
      #self.text_item = text_item
      username = self.canvas.itemcget(text_item_user, 'text')
      print(f"{username}")
      query = "SELECT email FROM account WHERE username LIKE %s "
      cursor = self.db.execute_query(query, ('%' + username + '%',))
      info = cursor.fetchall()
      email = info
      print(f"user email :{email}")
      return email
    
    def get_user(self, text_item):
       #self.num = int
       #if self.num == 1:
          friend_email = self.is_user(text_item)
          print(f"friend email: {friend_email}")
          return friend_email