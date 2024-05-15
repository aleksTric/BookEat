import mysql.connector


class Categories:
    def __init__(self, category):
        self.category_name = category
        
    def get_category(category):
        # Establish a connection to the MySQL database
        
        try:
            conn = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="bookeat"
            )
        
            cursor = conn.cursor()

            
            query = "SELECT COUNT(*) FROM categories WHERE category_name= %s"
            cursor.execute(query, (category,))
            categ_count = cursor.fetchone()[0]
            return categ_count > 0 
        
        except mysql.connector.Error as error:
            print("Failed to insert category:", error)   
        finally:
            
            if conn.is_connected():
               cursor.close()
               conn.close()    