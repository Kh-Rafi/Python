import mysql.connector

# 1. Connect directly to your local MySQL server
conn = mysql.connector.connect(host="localhost", user="root", password="your_password")

# 2. Open a cursor, execute the command, and close automatically
with conn.cursor() as cursor:
    cursor.execute("CREATE DATABASE IF NOT EXISTS my_easy_db")
    print("Database created successfully!")

conn.close()
