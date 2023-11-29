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
        inv = cur.execute(f"SELECT ISBN FROM " + self.tableName)
        inv_items = inv.fetchall()
        
        #displays all items in inventory
        if not self.tableName:
            print (f"Table not found")
        else :
            for ISBN in inv_items:
                itemDesc = cur.execute(f"SELECT * FROM " + self.tableName + " WHERE ISBN = " + ISBN)
                for desc in itemDesc:
                    print(desc)
        con.close()

        
    def searchInventory(self):
        #asks for title
        title = input("Enter a title: ")

        con = sqlite3.connect(self.databaseName)
        cur = con.cursor()
        titles = cur.execute(f"SELECT Title FROM " + self.tableName)
        
        #check if title in db
        if title in titles:
            titleDesc = cur.execute(f"SELECT * FROM " + self.tableName + " WHERE Title = " + title)
            for item in titleDesc:
                print(item + " ")
        else:
            print("Title not found")
        con.close()

    def decreaseStock(self, ISBN):

        #find isbn in table
        con = sqlite3.connect(self.databaseName)
        cur = con.cursor()
        isbn = cur.execute(f"SELECT ISBN FROM " + self.tableName+ " WHERE ISBN = " + ISBN)

        if not isbn:
            print("ISBN not found.")
        else:
            cur.execute(f"UPDATE Inventory SET Stock = (Stock - 1) WHERE ISBN = " + ISBN)
        con.close()











        
