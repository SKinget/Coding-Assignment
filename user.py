import sqlite3

class User:
    def __init__(self, databaseName='', tableName=''):
        self.databaseName = databaseName
        self.tableName = tableName
        self.userID = ''
        self.loggedIn = False
        self.conn = sqlite3.connect(self.databaseName)
        self.cursor = self.conn.cursor()
        
        
    def login(self):
        username = input("Username: ")
        password = input("Password: ")
        
        
    
    def logout(self):
        self.userID = ''
        self.loggedIn = False
        return False
        
    def viewAccountInformation(self):
        if not self.loggedIn:
            print("You are not logged in.")
            return
        
        self.cursor.excecute(f"SELECT * FROM {self.tableName} WHERE userID = ?", (self.userID))
        user_data = self.cursor.fetchone()
        
        if user_data is None:
            print("No data found for this user.")
        else:
            print("User Information:")
            for column, value in zip(self.cursor.description, user_data):
                print(f"{column[0]}: {value}")
    
    def createAccount(self):
        pass
    
    def getLoggedIn(self):
        return self.loggedIn
        
    def getUserID(self):
        return self.userID
