
class User:
    def __init__(self, canvas, db):
        self.canvas = canvas 
        self.db = db
    
    def is_user(self, text_item_user):
      username = self.canvas.itemcget(text_item_user, 'text')
      print(f"{username}")
      query = "SELECT email FROM account WHERE username LIKE %s "
      cursor = self.db.execute_query(query, ('%' + username + '%',))
      info = cursor.fetchall()
      email = info[0][0]
      print(f"user email :{email}")
      return email
    
   # def get_user(self, text_item):
    #    friend_email = self.is_user(text_item)
     #   print(f"friend email: {friend_email}")
      #  return friend_email
    
    #def get_user_library():