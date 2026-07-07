import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Niranjan@17",
    database="interview_system"
)

cursor = conn.cursor()

name = input("Enter Name: ")
email = input("Enter Email: ")


query = """
INSERT INTO candidates(name,email)
VALUES(%s,%s)
"""

cursor.execute(query,(name,email))

conn.commit()

print("Registration Successful")

conn.close()
