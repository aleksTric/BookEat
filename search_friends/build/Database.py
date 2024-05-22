import mysql.connector
from tkinter import messagebox

class Database:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database 
        self.conn = None

    def connect(self):
        try:
            self.conn = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            return self.conn
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Failed to connect to database: {err}")
            return None
        
    def close(self):
        if self.conn:
            self.conn.close()

    def execute_query(self, query, params=None):
        try:
            cursor = self.conn.cursor()
            cursor.execute(query, params)
            return cursor
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Failed to execute query: {err}")
            return None