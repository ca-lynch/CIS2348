# Cody Lynch
# 1954220

# Creates class ItemToPurchase
class ItemToPurchase:

    # Creates constructor for class ItemToPurchase with specified attributes
    def __init__(self, item_name='none', item_price=0, item_quantity=0, item_description='none'):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    # Creates print_item_cost method
    def print_item_cost(self):
        # Calculates and prints the cost per instructions
        string = '{} {} @ ${} = ${}'.format(self.item_name,
                                            self.item_quantity,
                                            self.item_price,
                                            (self.item_quantity * self.item_price))
        cost = self.item_quantity * self.item_price
        return string, cost

    # Creates print_item_description method
    def print_item_description(self):
        # Formats the description per instructions
        string = '{}: {}, %d oz.'.format(self.item_name,
                                         self.item_description,
                                         self.item_quantity)
        print(string)
        return string


# Creates class ShoppingCart
class ShoppingCart:

    # Creates constructor for class ShoppingCart with specified attributes
    def __init__(self, customer_name='none', current_date='January 1, 2016', cart_items=None):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = cart_items
        self.cart_items = []

    # Creates add_item method
    def add_item(self, item_to_purchase):
        # Adds item to the cart
        self.cart_items.append(item_to_purchase)

    # Creates remove_item method
    def remove_item(self, item_name):
        i = 0
        check = False
        # If loop determines if the item is in the cart
        for item in self.cart_items:
            # Removes item if it exists
            if item.item_name == item_name:
                del self.cart_items[i]
                check = True
                break
            i += 1
        # Alerts user if item is not found
        if not check:
            print('Item not found in cart. Nothing removed.')

    # Creates modify_item method
    def modify_item(self, item_to_purchase):
        check = None
        # Finds item and changes quantity
        for item in self.cart_items:
            if item.item_name == item_to_purchase.item_name:
                item.item_quantity = item_to_purchase.item_quantity
                check = True
                break
            else:
                check = False
        # Alerts user if item is not found
        if not check:
            print('Item not found in cart. Nothing modified.')

    # Creates get_num_items_in_cart method
    def get_num_items_in_cart(self):
        # Sentinel value
        num_items = 0
        # For loop calculates number of items in cart
        for item in self.cart_items:
            num_items = num_items + item.item_quantity
        return num_items

    # Creates get_cost_of_cart method
    def get_cost_of_cart(self):
        # Sentinel value
        total_cost = 0
        # For loop calculates cost
        for item in self.cart_items:
            cost = (item.item_quantity * item.item_price)
            # Updates total cost
            total_cost += cost
        return total_cost

    # Creates print_total method
    def print_total(self):
        # Outputs total of items in cart
        total_cost = self.get_cost_of_cart()
        if total_cost == 0:
            print('SHOPPING CART IS EMPTY')
        else:
            self.output_cart()

    # Creates print_descriptions method
    def print_descriptions(self):
        # Prints the customers name and date
        print('OUTPUT ITEMS\' DESCRIPTIONS')
        print('{}\'s Shopping Cart - {}'.format(self.customer_name,
                                                self.current_date), end='\n')
        print('\nItem Descriptions')
        # For loop prints the item descriptions
        for item in self.cart_items:
            print('{}: {}'.format(item.item_name, item.item_description))

    # Creates output_cart method
    def output_cart(self):
        # Prints a detailed list of the cart including cost
        print('OUTPUT SHOPPING CART')
        print('{}\'s Shopping Cart - {}'.format(self.customer_name,
                                                self.current_date))
        print('Number of Items: {}\n'.format(self.get_num_items_in_cart()))
        total_cost = 0
        for item in self.cart_items:
            print('{} {} @ ${} = ${}'.format(item.item_name,
                                             item.item_quantity,
                                             item.item_price,
                                             (item.item_quantity * item.item_price)))
            total_cost += (item.item_quantity * item.item_price)
        # Determines if cart is empty
        if len(self.cart_items) == 0:
            print('SHOPPING CART IS EMPTY')
        print('\nTotal: ${}'.format(total_cost))


# Creates the menu for the user
def print_menu(customer_cart):
    menu = ('\nMENU\n'
            'a - Add item to cart\n'
            'r - Remove item from cart\n'
            'c - Change item quantity\n'
            'i - Output items\' descriptions\n'
            'o - Output shopping cart\n'
            'q - Quit\n')
    # Sentinel value for nav variable
    nav = ''
    # As long as nav != q, the menu will be initialized
    while nav != 'q':
        print(menu)
        # Gets nav from user
        nav = input('Choose an option:\n')
        while nav != 'a' and nav != 'o' and nav != 'i' and nav != 'r' and nav != 'c' and nav != 'q':
            nav = input('Choose an option:\n')
        # Calls methods according to input
        if nav == 'a':
            print('ADD ITEM TO CART')
            # Gets item information from user
            item_name = str(input('Enter the item name:\n'))
            item_description = str(input('Enter the item description:\n'))
            item_price = int(input('Enter the item price:\n'))
            item_quantity = int(input('Enter the item quantity:\n'))
            item_to_purchase = ItemToPurchase(item_name, item_price, item_quantity, item_description)
            customer_cart.add_item(item_to_purchase)
        if nav == 'o':
            customer_cart.output_cart()
        if nav == 'i':
            customer_cart.print_descriptions()
        if nav == 'r':
            print('REMOVE ITEM FROM CART')
            # Gets item to be removed from user
            item_name = str(input('Enter name of item to remove:\n'))
            customer_cart.remove_item(item_name)
        if nav == 'c':
            print('CHANGE ITEM QUANTITY')
            # Gets item to be modified from user
            name = str(input('Enter the item name:\n'))
            # Gets new quantity from user
            quantity = int(input('Enter the new quantity:\n'))
            item_to_purchase = ItemToPurchase(item_name=name, item_quantity=quantity)
            customer_cart.modify_item(item_to_purchase)


if __name__ == '__main__':
    user_customer_name = str(input('Enter customer\'s name:\n'))
    user_current_date = str(input('Enter today\'s date:\n'))
    print('\nCustomer name:', user_customer_name)
    print('Today\'s date:', user_current_date)
    users_cart = ShoppingCart(user_customer_name, user_current_date)
    print_menu(users_cart)
