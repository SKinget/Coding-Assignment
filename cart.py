import sqlite3
import inventory as inv

    
class Cart:
    def __init__(self, database_name='', table_name=''):
        self.database_name = database_name
        self.table_name = table_name

    def view_cart(self, user_id, inventory_database):
        if not inventory_database:
            print("Error: Inventory database is not provided.")
            return

        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()

        cursor.execute("SELECT ISBN FROM {} WHERE userID = ?".format(self.table_name), (user_id,))
        cart_items = cursor.fetchall()

        if not cart_items:
            print("Cart is empty.")
        else:
            print(f"Viewing Cart for User: {user_id}")
            for item in cart_items:
                cursor.execute(f"SELECT Title FROM {inventory_database} WHERE ISBN = '{item[0]}'")
                item_title = cursor.fetchone()
                cursor.execute(f"SELECT Quantity FROM {self.table_name} WHERE ISBN = '{item[0]}'")
                item_quantity = cursor.fetchone()
                print(f"Title: {item_title[0]}, ISBN: {item[0]}, Quantity: {item_quantity[0]}")

        conn.close()

    # def view_cart(self, user_id, inventory_database):
    #     conn = sqlite3.connect(self.database_name)
    #     cursor = conn.cursor()

    #     cursor.execute("SELECT ISBN, quantity FROM {} WHERE userID = ?".format(self.table_name), (user_id,))
    #     cart_items = cursor.fetchall()

    #     if not cart_items:
    #         print("Cart is empty.")
    #     else:
    #         print(f"Viewing Cart for User: {user_id}")
    #         for item in cart_items:
    #             book_details = inventory_database.get_book_details(item[0])
    #             print(f"Title: {book_details['title']}, ISBN: {item[0]}, Quantity: {item[1]}")

    #     conn.close()

    def add_to_cart(self, user_id, ISBN):
        
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()
        
        cursor.execute("SELECT quantity FROM {} WHERE userID = ? AND ISBN = ?".format(self.table_name), (user_id, ISBN))
        existing_quantity = cursor.fetchone()
        
        if existing_quantity:
            new_quantity = existing_quantity[0] + 1
            cursor.execute("UPDATE {} SET quantity = ? WHERE userID = ? AND ISBN = ?".format(self.table_name), (new_quantity, user_id, ISBN))
        else:
            cursor.execute("INSERT INTO {} (userID, ISBN, quantity) VALUES (?, ?, ?)".format(self.table_name), (user_id, ISBN, 1))
            
        conn.commit()
        conn.close()
        print(f"Added {ISBN} to Cart for User: {user_id}")
        

    def remove_from_cart(self, user_id, ISBN):
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()

        cursor.execute("SELECT quantity FROM {} WHERE userID = ? AND ISBN = ?".format(self.table_name), (user_id, ISBN))
        existing_quantity = cursor.fetchone()

        if existing_quantity:
            if existing_quantity[0] > 1:
                new_quantity = existing_quantity[0] - 1
                cursor.execute("UPDATE {} SET quantity = ? WHERE userID = ? AND ISBN = ?".format(self.table_name), (new_quantity, user_id, ISBN))
                print(f"Removed 1 {ISBN} from the cart.")
            else:
                cursor.execute("DELETE FROM {} WHERE userID = ? AND ISBN = ?".format(self.table_name), (user_id, ISBN))
                print(f"Removed {ISBN} from the cart.")
        else:
            print(f"{ISBN} not found in the cart.")

        conn.commit()
        conn.close()

    # def check_out(self, user_id, inventory_database):
    #     conn = sqlite3.connect(self.database_name)
    #     cursor = conn.cursor()

    #     cursor.execute("SELECT ISBN, quantity FROM {} WHERE userID = ?".format(self.table_name), (user_id,))
    #     cart_items = cursor.fetchall()

    #     if not cart_items:
    #         print("Cart is empty. Nothing to check out.")
    #     else:
    #         for item in cart_items:
    #             inventory_database.decrease_stock(item[0], item[1])

    #         cursor.execute("DELETE FROM {} WHERE userID = ?".format(self.table_name), (user_id,))
    #         print(f"Checked out successfully. Cart is now empty.")

    #     conn.commit()
    #     conn.close()
    def check_out(self, user_id, inventory_database):
        #inv import
        i = inv.inv(self.database_name, inventory_database)
        if not inventory_database:
            print("Error: Inventory database is not provided.")
            return

        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()

        cursor.execute(f"SELECT ISBN, quantity FROM {self.table_name} WHERE userID = ?", (user_id,))
        cart_items = cursor.fetchall()

        if not cart_items:
            print("Cart is empty. Nothing to check out.")
        else:
            for item in cart_items:
                i.decreaseStock(item[0])

            cursor.execute(f"DELETE FROM {self.table_name} WHERE userID = ?", (user_id,))
            print(f"Checked out successfully. Cart is now empty.")

        conn.commit()
        conn.close()

