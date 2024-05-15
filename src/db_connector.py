#!/usr/bin/env /Applications/MAMP/Library/bin/python

import mysql.connector

config = {
    'user': 'root',
    'password': 'root',
    'host': '127.0.0.1',
    'unix_socket': '/Applications/MAMP/tmp/mysql/mysql.sock',
    'database': 'bookeat',  # Use the correct database name here
    'raise_on_warnings': True
}

try:
    # Attempt to connect to the database
    cnx = mysql.connector.connect(**config)
    print("Connected to the database!")

    # Create a cursor object
    cursor = cnx.cursor(dictionary=True)

    # Execute SQL queries
    # Fetch data from the dummy_table
    cursor.execute("SELECT * FROM dummy_table")
    rows = cursor.fetchall()

    # Print fetched data
    for row in rows:
        print(row)

except mysql.connector.Error as err:
    # Handle errors
    print(f"Error connecting to MySQL: {err}")

finally:
    # Close the connection
    if 'cnx' in locals():
        cnx.close()
