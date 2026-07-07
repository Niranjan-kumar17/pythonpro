import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Niranjan@17",
    database="interview_system"
)

cursor = conn.cursor()

# Candidate ID input
candidate_id = int(input("Enter Candidate ID: "))

# Questions fetch karo
cursor.execute("SELECT * FROM questions")
questions = cursor.fetchall()

score = 0

for q in questions:
    print("\nQuestion ID:", q[0])
    print("Question:", q[1])

    answer = input("Enter Answer: ").upper()

    if answer == q[2]:
        score += 1

print("\nYour Score:", score)

# Score update database me
update_query = """
UPDATE candidates
SET score = %s
WHERE candidate_id = %s
"""

cursor.execute(update_query, (score, candidate_id))
conn.commit()

print("Score Saved Successfully")

conn.close()
