import sqlite3
# cart.py
print("Script is running...")

class Cart:
    def __init__(self):
        self.database_name = ""
        self.table_name = ""

    def set_database_table(self, database_name, table_name):
        self.database_name = database_name
        self.table_name = table_name

    def view_cart(self, user_id, inventory_database):
        # Display all books in the user's cart
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()

        # Fetch cart items from the database
        cursor.execute(f"SELECT ISBN, quantity FROM {self.table_name} WHERE userID = ?", (user_id,))
        cart_items = cursor.fetchall()

        if not cart_items:
            print("Cart is empty.")
        else:
            print(f"Viewing Cart for User: {user_id}")
            for item in cart_items:
                book_details = inventory_database.get_book_details(item[0])
                print(f"Title: {book_details['title']}, ISBN: {item[0]}, Quantity: {item[1]}")

        conn.close()

    def add_to_cart(self, user_id, ISBN):
        # Add an item to the cart
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()

        # Check if the item is already in the cart
        cursor.execute(f"SELECT quantity FROM {self.table_name} WHERE userID = ? AND ISBN = ?", (user_id, ISBN))
        existing_quantity = cursor.fetchone()

        if existing_quantity:
            # Item is already in the cart, update the quantity
            new_quantity = existing_quantity[0] + 1
            cursor.execute(f"UPDATE {self.table_name} SET quantity = ? WHERE userID = ? AND ISBN = ?", (new_quantity, user_id, ISBN))
        else:
            # Item is not in the cart, add a new entry
            cursor.execute(f"INSERT INTO {self.table_name} (userID, ISBN, quantity) VALUES (?, ?, ?)", (user_id, ISBN, 1))

        conn.commit()
        conn.close()

        print(f"Added {ISBN} to Cart for User: {user_id}")

    def remove_from_cart(self, user_id, ISBN):
        # Remove an item from the cart
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()

        # Check if the item is in the cart
        cursor.execute(f"SELECT quantity FROM {self.table_name} WHERE userID = ? AND ISBN = ?", (user_id, ISBN))
        existing_quantity = cursor.fetchone()

        if existing_quantity:
            if existing_quantity[0] > 1:
                # Item is in the cart, decrease the quantity
                new_quantity = existing_quantity[0] - 1
                cursor.execute(f"UPDATE {self.table_name} SET quantity = ? WHERE userID = ? AND ISBN = ?", (new_quantity, user_id, ISBN))
                print(f"Removed 1 {ISBN} from the cart.")
            else:
                # Last item of this type, remove the entry from the cart
                cursor.execute(f"DELETE FROM {self.table_name} WHERE userID = ? AND ISBN = ?", (user_id, ISBN))
                print(f"Removed {ISBN} from the cart.")
        else:
            print(f"{ISBN} not found in the cart.")

        conn.commit()
        conn.close()

    def check_out(self, user_id, inventory_database):
        # Check out the user, remove all cart items, and update inventory
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()

        # Fetch cart items for checkout
        cursor.execute(f"SELECT ISBN, quantity FROM {self.table_name} WHERE userID = ?", (user_id,))
        cart_items = cursor.fetchall()

        if not cart_items:
            print("Cart is empty. Nothing to check out.")
        else:
            for item in cart_items:
                # Assuming Inventory class has a method to decrease stock
                inventory_database.decrease_stock(item[0], item[1])

            # Remove all items from the cart after checking out
            cursor.execute(f"DELETE FROM {self.table_name} WHERE userID = ?", (user_id,))
            print(f"Checked out successfully. Cart is now empty.")

