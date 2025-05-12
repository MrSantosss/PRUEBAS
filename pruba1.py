#The list that would be the shopping cart is defined and products that would already be in the inventory by default are added.
inventory = [{"name":"parasol","price":10000 , "units": 10} , {"name":"waterproof","price":5000 , "units": 20}, {"name":"bags","price":500 , "units": 50}, {"name":"ice_cream","price":3500 , "units": 10}, {"name":"gum","price":200 , "units": 30} ]

#The enter function is the one that requests the data of the product you want to add, every time the enter function is invoked, a new dictionary is created and stores them all in the cart list
def enter (): 
    try:
      
     name = input(" Enter the Product to Add : ").lower().strip()
     price = float(input(" Enter the Unit Price of the Product: "))
     if price < 0 :
         print (" \nEnter a Positive Value\n ")
         return enter()
     units = int(input(" Enter the Quantity of units of the Product : "))
     if units <= 0 :
         print (" \nenter a valid amount\n")
         return enter()
     inventory.append({"name":name,"price":price,"units":units})
    except ValueError:
        print("\n Invalid data entered\n ")
#The search function runs through the entire list and the dictionaries within it and if it is found it returns a value and it would be true, and if not it returns an empty being false and if it is false it says that it is not there and if it is true it shows the product with price and units
def search ():
    producttosearch = input(" Enter the Product you want to Search : ").lower()
    for product in inventory:
        if producttosearch == product["name"] :
            print(" The Product is in the Inventory ")
            return product
    return None
#the update function scans the cart and if it finds that the product is the same as the input that was entered, the new price is requested to update it and the old price is changed to the new one. If none is found, the user is told that it is not in the cart and to try entering the product first.
def update ():
    try:
        i = 0 
        producttosearch = input(" Enter the Product you want to Update : ").lower().strip()
        for product in inventory:
            if producttosearch == product["name"] :
                i += 1
                nvprice = float(input("Enter the new price of the Product: "))
                if nvprice < 0 :
                    print (" Enter a Positive Value ")
                    return update()
                else :
                    product["price"] = nvprice 
                    print(" \nPrice updated correctly")
                    break
        if i <= 0:
            print(" The Product to Update is not in the Inventory")
            print(" The Product was not found in the Inventory, try to enter it first")
    except ValueError:
        print(" Invalid data entered ")
#What the eliminate function does is that it goes through the list and if an identical data is found in the dictionaries of the list, it eliminates the entire dictionary that has that data, thus eliminating both the name, price and units
def eliminate (): 
    i=0
    Pelim = input(" Enter the Product You Want to Delete : ").lower().strip()
    for product in inventory:
        
        if Pelim == product["name"]:
            i =+ 1
            inventory.remove(product)
            print("\n\n The product has been successfully removed\n")
            break
    if i <= 0 :
        print(" The Product is not in the Inventory ")
#The show function prints the entire inventory and the sum total of the price of everything
def show () :
    for show in inventory :
        print (show)    
    total= sum(map(lambda p :p["price"] * p["units"] , inventory))
    print (f" Total : {total:.2f}")
#the main menu is already printed the main message of the menu and the options to enter, it is inside a cycle so that as long as you do not enter the exit option it returns and is shown to continue modifying or adding things to the program.
while True :
    try:
     print("\n\n","*"*40)
     menu = int(input(f"\n          MENU\n   Option 1: Add Products to the Inventory \n   Option 2: Check Products in the Inventory \n   Option 3: Update a Product Price \n   Option 4: Delete a Product from the Inventory \n   Option 5: See the Inventory and its Total Price \n   Option 6: Exit the Program \n   Enter the Option you want to Perform: "))
     print("\n\n","*"*40)
     if menu == 1 : 
      enter ()
     elif menu == 2: 
        searched_product = search ()
        if searched_product:
            print(searched_product)
        else:
            print("\nThe Product is not in Inventory\n")
     elif menu == 3 :
       update()
     elif menu == 4 :
        eliminate()
     elif menu == 5 :
        show()
     elif menu == 6 :
        print("\n Thank you for using our program \n")
        break
     else:
         print("\nenter a valid option  ( 1 - 6 )\n")
    except ValueError:
        print(" Invalid data entered ")
