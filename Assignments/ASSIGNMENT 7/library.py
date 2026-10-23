import sqlite3

conn = sqlite3.connect("library.db")

cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS books")

cursor.execute("""
CREATE TABLE books (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    year INTEGER,
    genre TEXT,
    copies INTEGER,
    rating INTEGER
)
""")

cursor.execute("""
INSERT INTO books
(id, title, author, year, genre, copies, rating)
VALUES (1, 'Harry Potter', 'J.K. Rowling', 1997, 'Fiction', 5, 5)
""")

books = [
    (2, "The Hobbit", "J.R.R. Tolkien", 1937, "Fiction", 3, 4),
    (3, "Sherlock Holmes", "Arthur Conan Doyle", 1892, "Mystery", 2, 5),
    (4, "A Brief History of Time", "Stephen Hawking", 1988, "Science", 3, None),
    (5, "Sapiens", "Yuval Noah Harari", 2011, "History", 4, 5),
    (6, "The Silent Patient", "Alex Michaelides", 2019, "Mystery", 2, None),
    (7, "The Selfish Gene", "Richard Dawkins", 1976, "Science", 3, 4),
    (8, "To Kill a Mockingbird", "Harper Lee", 1960, "Fiction", 4, 5)
]

cursor.executemany("""
INSERT INTO books
(id, title, author, year, genre, copies, rating)
VALUES (?, ?, ?, ?, ?, ?, ?)
""", books)

conn.commit()

print("\nBooks published after 1990:")

cursor.execute("SELECT title, author FROM books WHERE year > 1990")

for book in cursor.fetchall():
    print(book[0], "-", book[1])
    
print("\nFiction books with more than 2 copies:")

cursor.execute("SELECT title FROM books WHERE genre = 'Fiction' AND copies > 2")

for book in cursor.fetchall():
    print(book[0])

print("\nBooks published before 1900 OR rated 5:")

cursor.execute("SELECT title FROM books WHERE year < 1900 OR rating = 5")

for book in cursor.fetchall():
    print(book[0]) 

print("\nBooks not in Mystery genre:")

cursor.execute("SELECT title FROM books WHERE NOT genre = 'Mystery'")

for book in cursor.fetchall():
    print(book[0])

print("\nBooks in Science or History genre:")

cursor.execute("SELECT title FROM books WHERE genre IN ('Science', 'History')")

for book in cursor.fetchall():
    print(book[0])

letter = input("\nEnter a letter to search authors: ").strip()

print("\nAuthors whose names start with", letter + ":")

cursor.execute("SELECT author FROM books WHERE author LIKE ?", (letter + "%",))

for book in cursor.fetchall():
    print(book[0])

print("\nBooks with no rating:")

cursor.execute("SELECT title FROM books WHERE rating IS NULL")

for book in cursor.fetchall():
    print(book[0])

conn.close()
