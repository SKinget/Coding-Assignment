import sqlite3

# Connect to the database
connection = sqlite3.connect('Ecommerce.db')

# Create a cursor object to execute SQL commands
cursor = connection.cursor()

# Define the Inventory table schema
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Inventory (
        ISBN TEXT PRIMARY KEY,
        Title TEXT,
        Author TEXT,
        Genre TEXT,
        Pages INTEGER,
        ReleaseDate TEXT,
        Stock INTEGER
    )
''')

# Define the Cart table schema
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Cart (
        UserID TEXT,
        ISBN TEXT,
        Quantity INTEGER,
        FOREIGN KEY (UserID) REFERENCES User(UserID),
        FOREIGN KEY (ISBN) REFERENCES Inventory(ISBN),
        PRIMARY KEY (UserID, ISBN)
    )
''')

# Define the User table schema
cursor.execute('''
    CREATE TABLE IF NOT EXISTS User (
        UserID TEXT PRIMARY KEY,
        Email TEXT,
        Password TEXT,
        FirstName TEXT,
        LastName TEXT,
        Address TEXT,
        City TEXT,
        State TEXT,
        Zip TEXT
    )
''')

# Query to check existing tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

# Display the tables
print("Tables in the database:")
for table in tables:
    print(table[0])
    
# Commit the changes and close the connection
connection.commit()
connection.close()
