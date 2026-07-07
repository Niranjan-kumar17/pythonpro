import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Niranjan@17",
    database="interview_system"
)

cursor = conn.cursor()

cursor.execute("SELECT * FROM candidates")

data = cursor.fetchall()

print("\nCandidate Results")
print("-" * 50)

for row in data:
    print("ID:", row[0])
    print("Name:", row[1])
    print("Email:", row[2])
    print("Score:", row[3])
    print("-" * 50)

conn.close()
