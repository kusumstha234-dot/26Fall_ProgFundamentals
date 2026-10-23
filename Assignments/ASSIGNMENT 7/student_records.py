import sqlite3

conn = sqlite3.connect("StudentRecords.db")

cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS StudentRecords")

cursor.execute("""
CREATE TABLE StudentRecords (
    ID INTEGER PRIMARY KEY,
    Name TEXT,
    Age INTEGER,
    Major TEXT
)
""")

students = [
    (1, "John", 20, "Computer Science"),
    (2, "Emma", 21, "Business"),
    (3, "Michael", 22, "Engineering"),
    (4, "Sophia", 19, "Biology"),
    (5, "David", 23, "Mathematics")
]

cursor.executemany("""
INSERT INTO StudentRecords (ID, Name, Age, Major)
VALUES (?, ?, ?, ?)
""", students)

conn.commit()

print("\nStudent Records:")

cursor.execute("SELECT Name, Age, Major FROM StudentRecords")

for student in cursor.fetchall():
    print(student[0], "-", student[1], "-", student[2])

print("\nStudents older than 20:")

cursor.execute("SELECT Name, Age FROM StudentRecords WHERE Age > 20")

for student in cursor.fetchall():
    print(student[0], "-", student[1])

print("\nStudents majoring in Computer Science:")

cursor.execute("SELECT Name FROM StudentRecords WHERE Major = 'Computer Science'")

for student in cursor.fetchall():
    print(student[0])

print("\nStudents younger than 22:")

cursor.execute("SELECT Name, Age FROM StudentRecords WHERE Age < 22")

for student in cursor.fetchall():
    print(student[0], "-", student[1])

print("\nStudents majoring in Business or Engineering:")

cursor.execute("SELECT Name, Major FROM StudentRecords WHERE Major IN ('Business', 'Engineering')")

for student in cursor.fetchall():
    print(student[0], "-", student[1])

print("\nStudents whose names start with J:")

cursor.execute("SELECT Name FROM StudentRecords WHERE Name LIKE 'J%'")

for student in cursor.fetchall():
    print(student[0])

print("\nStudents not majoring in Business:")

cursor.execute("SELECT Name, Major FROM StudentRecords WHERE Major != 'Business'")

for student in cursor.fetchall():
    print(student[0], "-", student[1])

print("\nStudents aged between 20 and 22:")

cursor.execute("SELECT Name, Age FROM StudentRecords WHERE Age BETWEEN 20 AND 22")

for student in cursor.fetchall():
    print(student[0], "-", student[1])

print("\nStudents sorted by age:")

cursor.execute("SELECT Name, Age FROM StudentRecords ORDER BY Age ASC")

for student in cursor.fetchall():
    print(student[0], "-", student[1])

print("\nStudents sorted by age (oldest first):")

cursor.execute("SELECT Name, Age FROM StudentRecords ORDER BY Age DESC")

for student in cursor.fetchall():
    print(student[0], "-", student[1])

print("\nTotal number of students:")

cursor.execute("SELECT COUNT(*) FROM StudentRecords")

total = cursor.fetchone()[0]

print("Total Students:", total)

print("\nAverage age of students:")

cursor.execute("SELECT AVG(Age) FROM StudentRecords")

average = cursor.fetchone()[0]

print("Average Age:", average)

print("\nYoungest and oldest student ages:")

cursor.execute("SELECT MIN(Age), MAX(Age) FROM StudentRecords")

result = cursor.fetchone()

print("Youngest Age:", result[0])
print("Oldest Age:", result[1])


print("\nSum of all students' ages:")

cursor.execute("SELECT SUM(Age) FROM StudentRecords")

total_age = cursor.fetchone()[0]

print("Total Age:", total_age)

print("\nNumber of students in each major:")

cursor.execute("SELECT Major, COUNT(*) FROM StudentRecords GROUP BY Major")

for student in cursor.fetchall():
    print(student[0], "-", student[1])

print("\nStudents older than the average age:")

cursor.execute("""
SELECT Name, Age FROM StudentRecords
WHERE Age > (SELECT AVG(Age) FROM StudentRecords)
""")

for student in cursor.fetchall():
    print(student[0], "-", student[1])

print("\nStudents aged 20 or 21:")

cursor.execute("SELECT Name, Age FROM StudentRecords WHERE Age IN (20, 21)")

for student in cursor.fetchall():
    print(student[0], "-", student[1])

print("\nStudents whose names contain the letter a:")

cursor.execute("SELECT Name FROM StudentRecords WHERE Name LIKE '%a%'")

for student in cursor.fetchall():
    print(student[0])

print("\nStudents whose ages are not between 20 and 22:")

cursor.execute("SELECT Name, Age FROM StudentRecords WHERE Age NOT BETWEEN 20 AND 22")

for student in cursor.fetchall():
    print(student[0], "-", student[1])

print("\nStudents majoring in Biology:")

cursor.execute("SELECT Name, Major FROM StudentRecords WHERE Major = 'Biology'")

for student in cursor.fetchall():
    print(student[0], "-", student[1])

print("\nStudents majoring in Mathematics:")

cursor.execute("SELECT Name, Major FROM StudentRecords WHERE Major = 'Mathematics'")

for student in cursor.fetchall():
    print(student[0], "-", student[1])

print("\nStudents aged 23 or older:")

cursor.execute("SELECT Name, Age FROM StudentRecords WHERE Age >= 23")

for student in cursor.fetchall():
    print(student[0], "-", student[1])

print("\nStudents aged 20 or younger:")

cursor.execute("SELECT Name, Age FROM StudentRecords WHERE Age <= 20")

for student in cursor.fetchall():
    print(student[0], "-", student[1])


answer = input("\nWould you like to add a new student? (yes/no): ").strip().lower()

while answer not in ("yes", "no"):
    answer = input("Please enter yes or no: ").strip().lower()

if answer == "yes":
    name = input("Enter student name: ").strip()
    while not name:
        name = input("Name cannot be empty. Enter name: ").strip()

    while True:
        try:
            age = int(input("Enter student age: "))
            if age > 0:
                break
            print("Age must be positive.")
        except ValueError:
            print("Please enter a valid number.")

    major = input("Enter student major: ").strip()
    while not major:
        major = input("Major cannot be empty. Enter major: ").strip()

    cursor.execute(
        "INSERT INTO StudentRecords (Name, Age, Major) VALUES (?, ?, ?)",
        (name, age, major)
    )

    conn.commit()
    print("Student added successfully!")
else:
    print("No new student added.")


conn.close()