class FriendsList:
   def __init__ (self, canvas, db, sender_id, receiver_id, status):
      self.canvas = canvas 
      self.db = db
      self.sender_id = sender_id
      self.receiver_id = receiver_id

   def add_friend(self):
      query = "INSERT INTO friendslist(sender_id, receiver_id) VALUES (%s, %s) "
      self.db.execute_query(query, (self.sender_id, self.receiver_id))
      self.db.commit_query
