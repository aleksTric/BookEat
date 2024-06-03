import mysql.connector
from tkinter import messagebox

class Database:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database 
        self.conn = None

    def connect_to_database(self):
        try:
            self.conn = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if self.conn.is_connected():
                print("successfully connected to database")
            return self.conn
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Failed to connect to database: {err}")
            return None
        
    def disconnect_to_database(self):
        if self.conn:
            self.conn.close()

    def commit_query(self):
        if not self.conn:
            self.connect_to_database()
            if not self.conn:
                return None
        if self.conn:
            self.conn.commit()
            return 1

    def execute_query(self, query, params=None):
        try:
            cursor = self.conn.cursor()
            cursor.execute(query, params)
            
            return cursor
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Failed to execute query: {err}")
            return None
        
    def retrieve_data(self, canvas, db, text1, text2, text3, text4, text5, text6):
       self.canvas = canvas 
       self.db = db
       query = "SELECT username FROM account"
       cursor = self.db.execute_query(query)
       rows = cursor.fetchall()
       
       self.canvas.itemconfig(text1, text=rows[0])
       self.canvas.itemconfig(text2, text=rows[1])
       self.canvas.itemconfig(text3, text=rows[2])
       self.canvas.itemconfig(text4, text=rows[3])
       self.canvas.itemconfig(text5, text=rows[4])
       self.canvas.itemconfig(text6, text=rows[5])