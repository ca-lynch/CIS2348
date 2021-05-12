# Cody Lynch
# 1954220

import csv  # Imports csv module
import sys
from datetime import date, datetime  # Imports datetime module


class InventoryItem:  # Creates class to store item information for each item
    serial_num = int()
    manufacturer = str()
    product_type = str()
    damage_status = False
    price = int()
    service_date = str()

    # Construct for InventoryItem class
    def __init__(self, serial_num, manufacturer, product_type, damage_status, price=int(), service_date=""):
        self.serial_num = serial_num
        self.manufacturer = manufacturer.strip()  # Had to sanitize input files to get accurate data
        self.product_type = product_type
        self.damage_status = damage_status
        self.price = price
        self.service_date = service_date


class InventoryItems:  # Creates class to work through CSV files
    inventoried_items = []

    def __init__(self):  # Construct for InventoryItems
        self.manufacturer_csv()
        self.price_csv()
        self.service_csv()

    def manufacturer_csv(self):  # Function for ManufacturerList.csv
        with open('ManufacturerList.csv', newline='') as csv_manufacturer:  # Opens the csv file
            csv_manufacturer = csv.reader(csv_manufacturer)
            for row in csv_manufacturer:  # Identifies which items are damaged with boolean
                damaged = False  # Defaults as not damaged
                if row[3] != "":
                    damaged = True  # If item is labeled as damaged in file, changes damage status
                item = InventoryItem(serial_num=row[0],  # Sets values to item variable for output
                                     manufacturer=row[1],
                                     product_type=row[2],
                                     damage_status=damaged)
                self.inventoried_items.append(item)
        return InventoryItems.inventoried_items

    def price_csv(self):  # Function for PriceList.csv
        with open('PriceList.csv', newline='') as csv_price:
            csv_price = csv.reader(csv_price)
            for row in csv_price:
                item = self.find_serial(row[0])  # Identifies the item serial number with find_serial function
                item.price = row[1]  # Identifies the item price

    def find_serial(self, serial_num):  # Function for finding the serial number
        for item in self.inventoried_items:
            if item.serial_num == serial_num:
                return item

    def service_csv(self):  # Function for ServiceDatesList.csv
        with open('ServiceDatesList.csv', newline='') as csv_service:
            csv_service = csv.reader(csv_service)
            for row in csv_service:
                item = self.find_serial(row[0])  # Identifies item serial number with find_serial function
                item.service_date = row[1]  # Identifies the item service date

    def damaged_list(self):  # Creates the DamagedInventory.csv file, holds damaged items
        f = open("DamagedInventory.csv", "w")  # Creates a new file, or updates an existing file
        damaged_items = []  # Empty list as sentinel value
        for i in self.inventoried_items:
            if i.damage_status:  # Puts damaged items into damaged_items list
                damaged_items.append(i)
        sorted2 = sorted(damaged_items, key=lambda x: int(x.price), reverse=True)  # Sorts the items in the csv by price
        for item in sorted2:
            f.write(self.damaged_item_print(item))  # Adds items into output through damaged_item_price function
        f.close()  # Closes file

    @staticmethod
    def damaged_item_print(item: InventoryItem):  # Function for outputting damaged items
        return item.serial_num + "," + item.manufacturer + "," + item.product_type + "," + str(item.price) + "," + \
               item.service_date + "\n"

    def full_list(self):  # Creates the FullInventory.csv file, holds the entire inventory
        f = open("FullInventory.csv", "w")
        # Sorts items in the csv alphabetically by manufacturer, descending
        sorted_items = sorted(inventory.inventoried_items, key=lambda x: x.manufacturer, reverse=False)
        for item in sorted_items:
            f.write(self.full_item_string(item))  # Adds items to output through full_item_print function
        f.close()  # Closes file

    @staticmethod
    def full_item_string(i: InventoryItem):  # Print function for the FullInventory.csv
        damaged = str()  # Sentinel value for damage status
        if i.damage_status:
            damaged = "damaged"  # Changes value for damaged status if the damage status=True
        return "{},{},{},{},{},{}\n".format(i.serial_num, i.manufacturer, i.product_type, str(i.price),
                                            i.service_date, damaged)  # Outputs the full inventory per instructions

    @staticmethod
    def your_item_is_string(i: InventoryItem):  # Outputs the item user looked for
        return "Your item is: {} {} {} ${}\n".format(i.serial_num, i.manufacturer, i.product_type, str(i.price))

    @staticmethod
    def your_item_is_close_to_string(i: InventoryItem):  # Outputs item similar to users search
        return "You may also consider: {} {} {} ${}\n".format(i.serial_num, i.manufacturer, i.product_type,
                                                              str(i.price))

    @staticmethod
    def print_search_result(user_input):  # Function to print results from user search
        exact_items_to_print = []
        close_items_to_print = []
        all_items = inventory.inventoried_items
        price_sentinel = sys.maxsize  # This number happens to be 9223372036854775807
        user_suggested_item = InventoryItem("", "", "", "")
        for y in all_items:  # Finds exact match to user search
            if InventoryItems.item_exact_parser(user_input, y) is not None:
                exact_items_to_print.append(y)
        for y in all_items:  # Finds items close to user search based off product type
            if InventoryItems.item_close_to_parser(user_input, y) is not None:
                close_items_to_print.append(y)
        if len(exact_items_to_print) > 0:  # Checks for exact matches
            highest_price_item = InventoryItem("", "", "", "")  # Default values for item
            for x in exact_items_to_print:  # Finds the highest priced item that exists
                if int(highest_price_item.price) < int(x.price):
                    highest_price_item = x
            print(InventoryItems.your_item_is_string(highest_price_item))  # Prints highest priced item from search
            current_price = highest_price_item.price  # Value to find nearest price
            for x in close_items_to_print:  # Finds absolute distance between similar product prices
                closest_price = abs(int(x.price) - int(current_price))
                if price_sentinel > closest_price:  # This will always be true
                    price_sentinel = closest_price  # Changes sentinel value to the calculated price
                    user_suggested_item = x  # Sets an item to suggest to user
            print("You may, also, consider: {} {} {} ${}" .format(user_suggested_item. serial_num,
                                                                  user_suggested_item.manufacturer,
                                                                  user_suggested_item.product_type,
                                                                  user_suggested_item.price))
        else:
            print("No such item in inventory")  # Lets user know item is not in inventory
            if len(close_items_to_print) > 0:
                highest_price_item = InventoryItem("", "", "", "")
                for x in close_items_to_print:  # This will give user a similar item
                    if int(highest_price_item.price) < int(x.price):
                        highest_price_item = x
                print(InventoryItems.your_item_is_close_to_string(highest_price_item))

    @staticmethod
    def item_exact_parser(u, item):  # Parsing function to find exact matches per user search
        search_values = set(u.lower().split(" "))  # Sets users input to lowercase and splits values
        manufacturer_list = [item.manufacturer.lower()]  # List of manufacturers to parse
        product_type_list = [item.product_type.lower()]  # List of product types to parse
        manufacturer_set = set(manufacturer_list)  # 152 & 153 create sets to be evaluated
        product_type_set = set(product_type_list)
        matches_manufacturer = manufacturer_set.intersection(search_values)  # Intersection finds matching values
        matches_product_type = product_type_set.intersection(search_values)
        if len(matches_manufacturer) == 1 and len(matches_product_type) == 1:  # Checks if manufacturer and product
            if not item.damage_status:                                         # type matches, checks the damage
                if not InventoryItems.is_service_date_before_today(item):      # status, and service date
                    return item
        return None

    @staticmethod
    def item_close_to_parser(u, item):  # Parsing function to find similar items to user search
        search_values = set(u.lower().split(" "))  # Sets user input to lowercase and splits values
        product_type_list = [item.product_type.lower()]  # List of product types to parse
        product_type_set = set(product_type_list)  # Creates set to be evaluated
        matches_product_type = product_type_set.intersection(search_values)  # Intersection finds matching values
        if len(matches_product_type) == 1 and item.manufacturer.lower() not in search_values:  # Finds items that
            if not item.damage_status:                                           # have the same product type
                if not InventoryItems.is_service_date_before_today(item):        # but different manufacturers
                    return item
        return None

    def type_csv(self):  # This function creates inventory files for each type of product in the full inventory
        type_set = set()  # Creates empty set to store product types
        for i in self.inventoried_items:
            type_set.add(i.product_type)  # Adds each type of product into the set
        for item_type in type_set:
            f = open(item_type.capitalize() + "Inventory.csv", "w")  # Creates a file for each product type
            item_types = []
            for i in self.inventoried_items:
                if i.product_type == item_type:
                    item_types.append(i)
            sorted_items = sorted(item_types, key=lambda x: int(x.serial_num), reverse=False)  # Sorts items by serial
            for item in sorted_items:                                                          # number ascending
                f.write(self.type_item_print(item))  # Adds items to output through type_item_print function
            f.close()  # Closes file

    @staticmethod
    def type_item_print(item: InventoryItem):  # Print function for [type]Inventory.csv
        damaged = str()  # Sentinel value for damage status
        if item.damage_status:  # Changes status to "damaged" if damage_status=True
            damaged = "damaged"
        return "{},{},{},{},{}\n".format(item.serial_num, item.manufacturer, str(item.price),  # Outputs item info
                                         item.service_date, damaged)

    @staticmethod
    def is_service_date_before_today(item: InventoryItem):  # Function for comparing dates
        today = date.today()  # Finds the current date
        month, day, year = map(int, item.service_date.split('/'))  # Sets format for date
        date1 = date(year, month, day)  # Service date
        return date1 <= today  # Determines if date has passed or not

    @staticmethod
    def time_in_milli(item: InventoryItem):  # Function for converting datetime into milliseconds for comparing dates
        month, day, year = map(int, item.service_date.split('/'))  # Formats date
        date1 = datetime(year, month, day)
        return date1.timestamp()  # Returns datetime in milliseconds

    def call_date(self):  # Function for adding past dates into csv file
        past_dates = []  # Default empty list to add dates to
        for i in self.inventoried_items:
            if self.is_service_date_before_today(i):  # Uses is_service_date_before_today function to add dates to list
                past_dates.append(i)
        f = open("PastServiceDateInventory.csv", "w")  # Creates csv for items that have been serviced
        sorted_items = sorted(past_dates, key=lambda x: self.time_in_milli(x), reverse=False)  # Sorts items by date
        for item in sorted_items:                                                              # recent to oldest
            f.write(self.full_item_string(item))  # Uses full_item_print function to output items as its the same format
        f.close()  # Closes file


def print_menu():
    menu = ('\n    MAIN MENU\n'
            's - Search for item\n'
            'q - Quit')
    nav = ''
    while nav != 'q':
        print(menu)
        nav = input("\nChoose an option:\n")
        if nav == 's' or nav == 'S':
            print('    Item Lookup:')
            user_input = input("Enter item manufacturer and type:\n")
            InventoryItems.print_search_result(user_input)
        if nav == 'q' or nav == 'Q':
            break


# Calls the various functions
inventory = InventoryItems()  # Called for project part one and two
print_menu()                  # Called for project part two
