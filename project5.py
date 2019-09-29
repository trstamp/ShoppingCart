# Tyler Stamp
# Project 5
# 11/19/18

class ItemToPurchase():
    total = 0
    prices = [3,128]
    quantities = [5,1]
    def __init__(self, name = 'none', price = 0, quantity = 0, desc = 'none'):
        self.item_name = str(name)
        self.item_price = float(price)
        self.item_quantity = int(quantity)
        self.item_description = str(desc)

    def print_item_cost(self):
        print(name,quantity,"@ $",price,"= $",int(price * quantity))

    def print_item_description(self):
        i = 0
        for name in ShoppingCart().cart_items:
            print(name,": ",ShoppingCart().descriptions[i])
            i = i + 1

    def prices_method(self, price):
        ItemToPurchase().prices.append(price)
        total = float(sum(ItemToPurchase().prices))
        print("Total: $",total)


class ShoppingCart():

    item = ItemToPurchase()
    cart_items = ['Chocolate Chips','Powerbeats 2 Headphones']
    descriptions = ['Semi-sweet','Bluetooth headphones']
    customer = ''
    date = ''

    def __init__(self, customer = 'none', date = 'January 1, 2016'):
        self.customer_name = str(customer)
        self.current_date = str(date)

    def add_item(self):
        newItem = str(input("What item would you like to add? "))
        ShoppingCart().cart_items.append(newItem)
        itemDesc = input("What is the item description? ")
        ShoppingCart().descriptions.append(itemDesc)
        pr = float(input("What is the price? "))
        ItemToPurchase().prices_method(pr)
        qt = int(input("What is the quantity? "))
        ItemToPurchase().quantities.append(qt)


    def remove_item(self):
        print("REMOVE ITEM FROM CART")
        rem = input("Which item would you like to remove? ")
        i = 0
        while(i < len(ItemToPurchase().quantities)):
            if(ShoppingCart().cart_items[i] == rem):
                ShoppingCart().cart_items.remove(rem)
                ShoppingCart().descriptions.remove(ShoppingCart().descriptions[i])
                ItemToPurchase().prices.remove(ItemToPurchase().prices[i])
                ItemToPurchase().quantities.remove(ItemToPurchase().quantities[i])
            else:
                i = i + 1

    def modify_item(self):
        print("1. description\n", "2. price\n", "3. quantity")
        mod = input("What would you like to modify? ")
        if(mod == '1' or mod == 'description'):
            print(ShoppingCart().descriptions)
            descIndex = int(input("Which index do you want to delete? "))
            ShoppingCart().descriptions.remove(ShoppingCart().descriptions[descIndex])
            itemDesc = input("What is the new item description? ")
            ShoppingCart().descriptions.insert(descIndex, itemDesc)
        elif(mod == '2' or mod == 'price'):
            print(ItemToPurchase().prices)
            priceIndex = int(input("Which index do you want to delete? "))
            ItemToPurchase().prices.remove(ItemToPurchase().prices[priceIndex])
            newPrice = input("What is the new price? ")
            ItemToPurchase().prices.insert(priceIndex, newPrice)
        elif(mod == '3' or mod == 'quantity'):
            print(ItemToPurchase().quantities)
            qIndex = int(input("Which index do you want to remove? "))
            ItemToPurchase().quantities.remove(ItemToPurchase().quantities[qIndex])
            newQ = input("What is the new quantity? ")
            ItemToPurchase().quantities.insert(qIndex, newQ)

    def get_num_items_in_cart(self):
        if(ItemToPurchase().quantity == 0):
            print("SHOPPING CART IS EMPTY")
        else:
            print("Number of items: ",sum(ItemToPurchase().quantity))

    def print_descriptions(self):
        i = 0
        while(i < len(ShoppingCart().descriptions)):
            print(ShoppingCart().cart_items[i],":",ShoppingCart().descriptions[i])
            i = i + 1

    def print_total(self):
        if(ItemToPurchase().quantities == 0):
            print("SHOPPING CART IS EMPTY")
        else:
            print(ShoppingCart().customer,"My Shopping Cart -", ShoppingCart().date)
            print("Number of items: ",sum(ItemToPurchase().quantities))
            i = 0
            for item in cart_items:
                print(item,ItemToPurchase().quantities,"@ $",ItemToPurchase().prices[i],"=", float(ItemToPurchase().prices[i]*ItemToPurchase().quantities))
            print("Total: ",float(sum(ItemToPurchase().prices)))

    def get_cost_of_cart(self):
        ItemToPurchase().prices_method()

class Main():

    def print_menu():
        print("MENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit")

        ans = input("Choose an option from the menu: ")

        while(len(ans) < 2):
            if(ans == 'a'):
                ShoppingCart().add_item()
            elif(ans == 'r'):
                ShoppingCart().remove_item()
            elif(ans == 'c'):
                ShoppingCart().modify_item()
            elif(ans == 'i'):
                print("ITEM DESCRIPTIONS\n")
                ItemToPurchase().print_item_description()
            elif(ans == 'o'):
                ShoppingCart().print_total()
            elif(ans == 'q'):
                print("Goodbye!")
                quit()
            else:
                print("invalid input")

            ans = input("Choose an option from the menu: ")

    print_menu()

Main()
