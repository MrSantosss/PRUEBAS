The Code is about a menu for :
Add Products to the Inventory
Check Products in the Inventory
Update a Product Price
Delete a Product from the Inventory
See the Inventory and its Total Price

Mainly a menu is generated in which all the functions of the menu and the code itself are listed.The code already comes with 5 predefined products with their respective price and quantity of products.Since the code already has predefined products, any function that appears in the menu can be performed.

The main function of the code is the menu that will always be displayed until the user wants to finish the program.Then there are the functionalities of the code that are:

The enter function, which is for entering new products into the inventory, asks you for the name, the price of each unit and the number of units of the product that will enter the inventory.

The search function is used to find a specific product in the inventory, it asks the name of the product you want to search in the inventory, if the product entered is not in the inventory it shows a message with that information, if the product that the person is looking for is in the inventory it shows the product with its price and units

The update function allows you to update the price of the product you enter, it asks you for the name of the product you want to update the price and if it is not in the inventory it shows you a message with that information, if the product is in the inventory it asks you for the new price of the product and it changes it, thus updating the price of the product

The delete function allows you to delete a product from the inventory. What this function does is ask you the product you want to delete from the inventory. If this product is not in the inventory, it shows you a message with that information. If the product is in the list, it deletes the product, thus eliminating its name, price and number of units.

The show function shows the user all the inventory and the total of all the products that are there

example of use:An example of use would be to enter two new products with option 1,Two new products are entered and then we click on option 5 to show the inventory and the total price of the inventory.
input example:

option 1 :
name:Chips       name:Soda
price:3000       price:2500
units:30         units:20


{'name': 'parasol', 'price': 10000, 'units': 10}
{'name': 'waterproof', 'price': 5000, 'units': 20}
{'name': 'bags', 'price': 500, 'units': 50}
{'name': 'ice_cream', 'price': 3500, 'units': 10}
{'name': 'gum', 'price': 200, 'units': 30}
{'name': 'chips', 'price': 3000.0, 'units': 30}
{'name': 'soda', 'price': 2500.0, 'units': 20}
 Total : 406000.0

example to use:The two new products are entered again with option 1.Then a product is removed from the inventory with option 4.and we also update the price of a product in the inventory with option 3,and then we see the inventory with option 5
input examnple :

option 1:
name:Chips       name:Soda
price:3000       price:2500
units:30         units:20

option 4 : parasol 

option 3 : waterproof
            5500


 {'name': 'waterproof', 'price': 5500.0, 'units': 20}
{'name': 'bags', 'price': 500, 'units': 50}
{'name': 'ice_cream', 'price': 3500, 'units': 10}
{'name': 'gum', 'price': 200, 'units': 30}
{'name': 'chips', 'price': 3000.0, 'units': 30}
{'name': 'soda', 'price': 2500.0, 'units': 20}
 Total : 316000.0

 Thanks :D
