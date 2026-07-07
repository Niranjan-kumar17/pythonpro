import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Niranjan@17",
    database="interview_system"
)

cursor = conn.cursor()

username = input("Enter Username: ")
password = input("Enter Password: ")

query = """
SELECT * FROM admin
WHERE username=%s AND password=%s
"""

cursor.execute(query, (username, password))

result = cursor.fetchone()

if result:
    print("Login Successful")
else:
    print("Invalid Username or Password")

conn.close()
