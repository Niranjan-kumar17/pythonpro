import mysql.connector
import time
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Niranjan@17",
    database="interview_system"
)

cursor = conn.cursor()
print("===== ADMIN LOGIN =====")

username = input("Username: ")
password = input("Password: ")

cursor.execute(
    "SELECT * FROM admin WHERE username=%s AND password=%s",
    (username, password)
)

admin = cursor.fetchone()

if admin:
    print("Login Successful")
else:
    print("Invalid Username or Password")
    exit()

while True:

    print("\n===== SMART INTERVIEW SYSTEM =====")
    print("1. Register Candidate")
    print("2. Start Test")
    print("3. View Results")
    print("4. Exit")

    choice = input("Enter Choice: ")

    # Register Candidate
    if choice == "1":

        name = input("Enter Name: ")
        email = input("Enter Email: ")

        cursor.execute(
            "INSERT INTO candidates(name,email) VALUES(%s,%s)",
            (name, email)
        )

        conn.commit()
        print("Registration Successful")

    # Start Test
    elif choice == "2":

        candidate_id = int(input("Enter Candidate ID: "))

        print("\nChoose Category")
        print("1. Python")
        print("2. SQL")
        print("3. Aptitude")

        cat_choice = input("Enter Choice: ")

        if cat_choice == "1":
            category = "Python"

        elif cat_choice == "2":
            category = "SQL"

        elif cat_choice == "3":
            category = "Aptitude"

        else:
            print("Invalid Category")
            continue

        cursor.execute(
            "SELECT * FROM questions WHERE category=%s",
            (category,)
        )

        questions = cursor.fetchall()

        if len(questions) == 0:
            print("No Questions Available")
            continue

        score = 0

        for q in questions:
            

            print("\nQuestion:", q[2])
            print("You have 10 seconds")

            start_time = time.time()

            answer = input("Enter Answer (A/B): ").upper()

            end_time = time.time()

            time_taken = end_time - start_time

            if time_taken > 10:
                
                print("Time Over!")
                continue

            if answer == q[3]:
                
                score += 1

        print("\nYour Score:", score)

        total_questions = len(questions)
        percentage = (score / total_questions) * 100

        if percentage >= 40:
            status = "PASS"
        else:
            status = "FAIL"

        print("Percentage:", percentage)
        print("Status:", status)

        cursor.execute(
            """
            UPDATE candidates
            SET score=%s, status=%s
            WHERE candidate_id=%s
            """,
            (score, status, candidate_id)
        )

        conn.commit()

        print("Result Saved Successfully")

    # View Results
    elif choice == "3":

        cursor.execute("""
            SELECT candidate_id,
                   name,
                   email,
                   score,
                   status
            FROM candidates
            ORDER BY score DESC
        """)

        data = cursor.fetchall()

        print("\n===== RESULTS =====")

        rank = 1

        for row in data:

            print(
                f"Rank: {rank} | "
                f"ID: {row[0]} | "
                f"Name: {row[1]} | "
                f"Email: {row[2]} | "
                f"Score: {row[3]} | "
                f"Status: {row[4]}"
            )

            rank += 1

    # Exit
    elif choice == "4":

        print("Thank You")
        break

    else:
        print("Invalid Choice")

conn.close()
