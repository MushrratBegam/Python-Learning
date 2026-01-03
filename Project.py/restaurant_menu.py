#  Define the menu of restaurant
menu = {
    'Pizza': 360,
    'Pasta': 70,
    'Veg spring roll': 120,
    'Paneer Tikka': 180,
    'Chiken Tandoori': 250,
    'French fries': 100,
    'Soup of the day': 90,
    'Coffee':80,
}
# Greet
print("Welcome to ZAIKA JUNCTION restaurant")
print("Pizza: RS-/360\npasta: RS-/70\nVeg spring roll: RS-/120\nPaneer Tikka: RS-/180\nChiken Tandoori: RS-/250\nFrench fries: RS-/100\nSoup of the day: RS-/90\nCoffee: RS-/80")

order_total = 0
while True:
  item = input("Enter the name of the item you want to order = ") 
    
  item_1 = input("Enter the name of the item you want to order = ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"your item {item_1} has been added to your order")
    
else:
    print(f"ordered item {item_1} is not available yet!")
    
another_order = input("Do you want to another item? (YES/NO) ")

if another_order == "yes":
    item_2 = input("Enter the name of second item = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2} has been added to order ")
    else:
        print(f"ordered item {item_2} is not availsble yet! ")
        
print(f"The total amount of item to pay is {order_total}")




    