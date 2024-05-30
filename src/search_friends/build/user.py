from notifications import Notifications

class User:
    def __init__(self, canvas, db):
        self.canvas = canvas 
        self.db = db
    
    def is_user(self, text_item_user):
      username = self.canvas.itemcget(text_item_user, 'text')
      query = "SELECT user_id FROM account WHERE username LIKE %s "
      cursor = self.db.execute_query(query, ('%' + username + '%',))
      info = cursor.fetchall()
      user_id = info[0][0]
      print(f"user {user_id}")
      return user_id
    
    def send_friend_req(self, text_friend, text_user):
       
       self.friend = User(self.canvas, self.db)
       self.logged_user = User(self.canvas, self.db)
       
       user_id = self.logged_user.is_user(text_user)
       friend_id = self.friend.is_user(text_friend)
       
       content = 'New Friend Request!!'
       status = 'not accepted'
       notification_type = 'friend request'

       friend_notification = Notifications(self.canvas, self.db)
       friend_notification.send_notification(user_id, friend_id, content, status, notification_type)
   
