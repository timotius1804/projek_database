import mysql.connector

# Establish the connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="inipassword"
)

mycursor = mydb.cursor()

# Drop and create the database
mycursor.execute("DROP DATABASE IF EXISTS LibraryDB")
mycursor.execute("CREATE DATABASE LibraryDB")
mycursor.execute("USE LibraryDB")

# Part 1: Create Tables
mycursor.execute("""
    CREATE TABLE Authors (
        AuthorID INT PRIMARY KEY AUTO_INCREMENT,
        FirstName VARCHAR(50) NOT NULL,
        LastName VARCHAR(50) NOT NULL,
        UNIQUE (FirstName, LastName)
    )
""")

mycursor.execute("""
    CREATE TABLE Books (
        BookID INT PRIMARY KEY AUTO_INCREMENT,
        Title VARCHAR(100) NOT NULL,
        AuthorID INT NOT NULL,
        PublishedYear YEAR,
        Genre VARCHAR(50),
        FULLTEXT (Title, Genre),
        FOREIGN KEY (AuthorID) REFERENCES Authors(AuthorID)
    )
""")

# Part 2: Insert Sample Data
authors_data = [
    ('J.K.', 'Rowling'),
    ('George R.R.', 'Martin'),
    ('J.R.R.', 'Tolkien')
]

books_data = [
    ("Harry Potter and the Sorcerer's Stone", 1997, 1, 'Fantasy'),
    ('A Game of Thrones', 1996, 2, 'Fantasy'),
    ('The Hobbit', 1937, 3, 'Fantasy')
]

mycursor.executemany("INSERT INTO Authors (FirstName, LastName) VALUES (%s, %s)", authors_data)
mycursor.executemany("INSERT INTO Books (Title, PublishedYear, AuthorID, Genre) VALUES (%s, %s, %s, %s)", books_data)
mydb.commit()

# Custom print function for readable output
def print_table(headers, rows, title=""):
    # Print the title if provided
    if title:
        print(f"\n{title.center(60, '-')}\n")

    # Print headers with a consistent width
    header_row = " | ".join(h.ljust(15) for h in headers)
    print(header_row)
    print("-" * len(header_row))

    # Print each row of data
    for row in rows:
        formatted_row = " | ".join(str(col).ljust(15) for col in row)
        print(formatted_row)

# Part 3: Count Books by Genre
mycursor.execute("""
    SELECT Genre, COUNT(*) AS BookCount
    FROM Books
    GROUP BY Genre
""")
books_by_genre = mycursor.fetchall()
print_table(['Genre', 'BookCount'], books_by_genre, "Books by Genre")

# Part 4: Join Tables
mycursor.execute("""
    SELECT b.Title, CONCAT(a.FirstName, ' ', a.LastName) AS Author
    FROM Books b
    INNER JOIN Authors a ON b.AuthorID = a.AuthorID
""")
books_authors = mycursor.fetchall()
print_table(['Title', 'Author'], books_authors, "Books and Authors")

# Part 5: Right Join
mycursor.execute("""
    SELECT b.Title, CONCAT(a.FirstName, ' ', a.LastName) AS Author
    FROM Books b
    RIGHT JOIN Authors a ON b.AuthorID = a.AuthorID
""")
books_authors_right = mycursor.fetchall()
print_table(['Title', 'Author'], books_authors_right, "Books and Authors (Right Join)")

# Part 6: Subquery to Find Authors with Books
mycursor.execute("""
    SELECT CONCAT(FirstName, ' ', LastName) AS AuthorName
    FROM Authors
    WHERE AuthorID IN (SELECT AuthorID FROM Books)
""")
authors_with_books = mycursor.fetchall()
print_table(['AuthorName'], authors_with_books, "Authors with Books")

# Close the cursor and connection
mycursor.close()
mydb.close()