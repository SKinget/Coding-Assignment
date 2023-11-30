import inventory as inv
import user as user
import cart as cart




#main

#seting classes
i = inv.inv('./Ecommerce.db', 'Inventory')
u = user.User('./Ecommerce.db', 'User')
c = cart.Cart('./Ecommerce.db', 'Cart')

#some variables for loops

on = 1
menuOption = 1
choice1 = '1'

print("Menu\n\n")
#before login
while (on == 1):
    while (menuOption == 1):
        print("1.Login\n2.Create Account\n3.Logout\n4.Exit")
        choice1 = input("Enter choice:")

        #login
        if (choice1 == '1'):
            print("Login")
            bool = u.login()
            if (bool == False):
                pass
            elif (bool == True):
                menuOption = 2
        #creat account
        elif (choice1 == '2'):
            print("Create account")
            u.createAccount()
            
        #logout
        elif (choice1 == '3'):
            print("Logout")
            u.logout()
            menuOption = 1
        #exit program 
        elif (choice1 == '4'):
            print("Exitting")
            menuOption = 0
            on = 0
            
        else:
            print("Invalid option")


    #After login main menu
    while (menuOption == 2):
        print("\nMain Menu\n")
        print("1.Logout\n2.View account information\n3.Inventory information\n4.Cart information\n")
        choice2 = input("Enter choice: ")

        #logout
        if (choice2 == "1"):
            print("Logging out")
            u.logout()
            menuOption = 1

        #view acc info
        elif (choice2 == "2"):
            print("Viewing account information")
            u.viewAccountInformation()

        #inv info
        elif (choice2 == "3"):
            print("Viewing inventory information")
            menuOption = 3
            
        #cart info
        elif (choice2 == "4"):
            print("Viewing cart information")
            menuOption = 4
        else:
            print("Invalid option")
            

    # after login inventory information
    while (menuOption == 3):
        print("\nInventory Information\n")
        print("1.Go back\n2.View inventory\n3.Search inventory\n")
        choice3 = input("Enter choice: ")
        
        #back
        if (choice3 == '1'):
            menuOption = 2

        #view inv
        elif (choice3 == '2'):
            print("Viewing inventory")
            i.viewInventory()

        #search inv
        elif (choice3 == '3'):
            print("Search inventory")
            i.searchInventory()
        else:
            print("Invalid option")



    # after login cart information
    while (menuOption == 4):
        print("\nCart Information\n")
        print("1.Go Back\n2.Search cart\n3.Add item to cart\n4.Remove item from cart\n5.Check out")
        choice4 = input("Enter choice: ")

        #back
        if (choice4 == '1'):
            menuOption = 2

        #view cart
        elif (choice4 == '2'):
            print("Viewing cart")
            c.view_cart(u.userID, i.tableName)
            
        #add item to cart
        elif (choice4 == '3'):
            print("Add item to cart")
            ISBN = input("Enter ISBN of item to add: ")
            c.add_to_cart(u.userID, ISBN)

        #remove item from cart
        elif (choice4 == '4'):
            print("Remove item from cart")
            ISBN = input("Enter ISBN of item to remove: ")
            c.remove_from_cart(u.userID, ISBN)

        #check out
        elif (choice4 == '5'):
            print("Checking out")
            c.check_out(u.userID, i.tableName)
            
        else:
            print("Invalid option")
    
