import sqlite3

class User:
    def __init__(self, databaseName='', tableName=''):
        self.databaseName = databaseName
        self.tableName = tableName
        self.userID = ''
        self.loggedIn = False
        
        
    def login(self):
        email = input("Email: ")
        password = input("Password: ")
        
        conn = sqlite3.connect(self.databaseName)
        cursor = conn.cursor()

        cursor.execute(f"SELECT * FROM {self.tableName} WHERE Email = '{email}' AND Password = '{password}'")
        user_data = cursor.fetchone()

        if user_data is not None:
            self.userID = user_data[0]
            self.loggedIn = True
            print("Login successful")
            return True;
        else:
            print("Invalid email or password")
            return False;

        conn.close()
        
        
    
    def logout(self):
        self.userID = ''
        self.loggedIn = False
        print("You have been logged out")
        return False
        
    def viewAccountInformation(self):
        if not self.loggedIn:
            print("You are not logged in.")
            return
        
        conn = sqlite3.connect(self.databaseName)
        cursor = conn.cursor()

        cursor.execute(f"SELECT * FROM {self.tableName} WHERE UserID = '{self.userID}'")
        user_data = cursor.fetchone()
        if user_data is None:
            print("No data found for this user")
        else:
            print("User Information:")
            for column, value in zip(cursor.description, user_data):
                print(f"{column[0]}: {value}")

        conn.close()
    
    def createAccount(self):
        conn = sqlite3.connect(self.databaseName)
        cursor = conn.cursor()
        
        email = input("Email: ")
        
        #check if userID exits
        userID = email
        cursor.execute(f"SELECT userID FROM {self.tableName} WHERE userID = '{userID}'")
        exist = cursor.fetchone()
        #if userID already exists
        if exist is not None:
            print("Account with this email already exists")

        else:
            password = input("Password: ")
            firstName = input("First Name: ")
            lastName = input("Last Name: ")
            address = input("Address: ")
            city = input("City: ")
            state = input("State: ")
            zip = input("Zip: ")
            
            cursor.execute(f"INSERT INTO {self.tableName} (UserID, Email, Password, FirstName, LastName, Address, City, State, Zip) VALUES ('{userID}', '{email}', '{password}', '{firstName}', '{lastName}', '{address}', '{city}', '{state}', '{zip}')")
            conn.commit()
            print("Account created successfully")
        conn.close()


    def getLoggedIn(self):
        return self.loggedIn
        
    def getUserID(self):
        return self.userID


