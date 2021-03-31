# Cody Lynch
# 1954220

# Creates class
class ItemToPurchase:

    # Creates constructor with attributes per instructions
    def __init__(self, item_name="none", item_price=0.0, item_quantity=0):
        self.item_name = str(item_name)
        self.item_price = float(item_price)
        self.item_quantity = int(item_quantity)

    # Creates method that calculates total price and outputs in correct format per instructions
    def print_item_cost(self):
        print("{} {} @ ${} = ${}".format(self.item_name,
                                         str(self.item_quantity),
                                         str(self.item_price),
                                         str(self.item_price * self.item_quantity)))


# This code came with the default template
if __name__ == "__main__":

    # Creates first instance of the class for object item1
    item1 = ItemToPurchase()

    # This print statement shows the user which item they are going to define
    print("Item 1")

    # Prompts user to define item1 attributes
    item1.item_name = input("Enter the item name:\n")
    item1.item_price = int(input("Enter the item price:\n"))
    item1.item_quantity = int(input("Enter the item quantity:\n"))

    # Creates second instance of the class for object item2
    item2 = ItemToPurchase()

    # This print statement shows the user which item they are going to define
    print("\nItem 2")

    # Prompts user to define item2 attributes
    item2.item_name = input("Enter the item name:\n")
    item2.item_price = int(input("Enter the item price:\n"))
    item2.item_quantity = int(input("Enter the item quantity:\n"))

    # This print statement begins the output for the total cost of items
    print("\nTOTAL COST")

    # Calls method to get the total cost of each item
    item1.print_item_cost()
    item2.print_item_cost()

    # Calculates total cost and sets that value to a variable
    total = (item1.item_price * item1.item_quantity) + (item2.item_price * item2.item_quantity)

    # Prints final total price of items
    print("\nTotal: $" + str(total))
