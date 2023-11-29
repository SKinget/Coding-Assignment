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
        
        
        cur.execute(f"SELECT ISBN FROM " + self.tableName)
        isbns = cur.fetchall()
        
        #displays all items in inventory
        if not self.tableName:
            print (f"Table not found")
        else :
            for isbn in isbns:
                cur.execute(f"SELECT * FROM {self.tableName} WHERE ISBN = '{isbn[0]}'")
                itemDesc = cur.fetchall()
                
                print("ISBN - Title - Author - Genre - Pages - Published - Stock")
                for value in zip(itemDesc):
                    print(f"{value[0]}")
        con.close()

        
    def searchInventory(self):
        #asks for title
        intitle = str(input("Enter a title: "))
        

        con = sqlite3.connect(self.databaseName)
        cur = con.cursor()
        cur.execute(f"SELECT * FROM {self.tableName} WHERE Title = '{intitle}'")
        titleDesc= cur.fetchone()
        
        
        #check if title in db
        if titleDesc is None:
            print("Title not found")
        else:
            for column, value in zip(cur.description, titleDesc):
                print(f"{column[0]}:{value}")
        con.close()

    def decreaseStock(self, ISBN):

        #find isbn in table
        con = sqlite3.connect(self.databaseName)
        cur = con.cursor()
        cur.execute(f"SELECT ISBN FROM {self.tableName} WHERE ISBN = '{ISBN}'")
        isbn = cur.fetchone()
        
        
        if isbn is None:
            print("ISBN not found.")
        else:
            cur.execute(f"SELECT Stock FROM {self.tableName} WHERE ISBN = '{ISBN}'")
            stock = cur.fetchone()
            stock = stock[0] - 1
            cur.execute(f"UPDATE {self.tableName} SET Stock = {stock} WHERE ISBN = '{ISBN}'")
        con.commit()
        con.close()





        
