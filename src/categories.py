import mysql.connector # type: ignore


class Categories:
    def __init__(self, category):
        self.__category_name = category
        
    def get_category_name(self):
        return self.__category_name
    
    def get_category(category):
        # Establish a connection to the MySQL database
        
        try:
            conn = mysql.connector.connect(
            host="127.0.0.1",
            user="kostas",
            password="kostas1234",
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

    def get_category_id(category):

        try:
            conn = mysql.connector.connect(
            host="127.0.0.1",
            user="kostas",
            password="kostas1234",
            database="bookeat"
            )
        
            cursor = conn.cursor()

            
            query = "SELECT category_id FROM categories WHERE category_name= %s"
            cursor.execute(query, (category,))
            categ_id = cursor.fetchone()
            
            if categ_id:
             return categ_id[0]  # Returning the category_id
            
            else:
             return None 
        
        except mysql.connector.Error as error:
            print("Failed to fetch category:", error)   
        finally:
            
            if conn.is_connected():
               cursor.close()
               conn.close()    