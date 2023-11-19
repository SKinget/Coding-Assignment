import sqlite3

class User:
    def __init__(self, databaseName='', tableName=''):
        self.databaseName = databaseName
        self.tableName = tableName
        self.userID = ''
        self.loggedIn = False
        
    def login(self):
        username = input("Username: ")
        password = input("Password: ")
        
        
    
    def logout(self):
        self.userID = ''
        self.loggedIn = False
        return False
        
    def viewAccountInformation)self):
        pass
    
    def createAccount(self):
        pass
    
    def getLoggedIn(self):
        return self.loggedIn
        
    def getUserID(self):
        return self.userID