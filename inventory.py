import sqlite3

class inv:
    def __init__(self,databaseName='',tableName=''):
        #zero constructor
        self.databaseName = databaseName
        self.tableName = tableName

        
    def setDatabaseName(self, databaseName):
        self.databaseName = databaseName

    def getDatabaseName(self):
        return self.databaseName
    
    def setTableName(self, tableName):
        self.tableName = tableName
        
    def getTableName(self):
        return self.tableName

    def viewInventory(self):
        
        con = sqlite3.connect(self.databaseName)
        cur = con.cursor()
        inv = cur.execute("SELECT PRIMARY KEY FROM " + self.tableName)
        inv_items = inv.fetchall()
        
        #displays all items in inventory
        if not tableName:
            print ("Table not found")
        else :
            for ISBN in inv_items:
                itemDesc = cur.execute("SELECT * FROM " + self.tableName + " WHERE ISBN = " + ISBN)
                for desc in itemDesc:
                    print(desc)
        
    def searchInventory(self):
        #asks for title
        title = input("Enter a title: ")

        con = sqlite3.connect(self.databaseName)
        cur = con.cursor()
        titles = cur.execute("SELECT Title FROM " + self.tableName)
        
        #check if title in db
        if title in titles:
            titleDesc = cur.execute("SELECT * FROM " + self.tableName + " WHERE Title = " + title)


    def decreaseStock(self, ISBN):

        #find isbn in table
        con = sqlite3.connect(self.databaseName)
        cur = con.cursor()
        isbn = cur.execute("SELECT ISBN FROM " + self.tableName+ " WHERE ISBN = " + ISBN)

        if not isbn:
            print("ISBN not found.")
        else:
            cur.execute("UPDATE Inventory SET Stock = (Stock - 1) WHERE ISBN = " + ISBN)












        
