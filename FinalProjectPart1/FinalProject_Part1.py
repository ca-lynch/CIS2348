# Cody Lynch
# 1954220

# Imports required modules
import csv
from datetime import date, datetime


# Creates class to store item information for each item
class InventoryItem:
    serial_num = int()
    manufacturer = str()
    product_type = str()
    damage_status = False
    price = int()
    service_date = str()

    # Construct for InventoryItem class
    def __init__(self, serial_num, manufacturer, product_type, damage_status, price=int(), service_date=""):
        self.serial_num = serial_num
        self.manufacturer = manufacturer
        self.product_type = product_type
        self.damage_status = damage_status
        self.price = price
        self.service_date = service_date


# Creates class to work through CSV files
class InventoryItems:
    inventoried_items = []

    # Construct for InventoryItems
    def __init__(self):
        self.manufacturer_csv()
        self.price_csv()
        self.service_csv()

    # Function for ManufacturerList.csv
    def manufacturer_csv(self):
        # Opens the csv file
        with open('ManufacturerList.csv', newline='') as csv_manufacturer:
            csv_manufacturer = csv.reader(csv_manufacturer)
            # Identifies which items are damaged with boolean
            for row in csv_manufacturer:
                # Defaults as not damaged
                damaged = False
                if row[3] != "":
                    # If item is labeled as damaged in file, changes damage status
                    damaged = True
                # Sets values to item variable for output
                item = InventoryItem(serial_num=row[0],
                                     manufacturer=row[1],
                                     product_type=row[2],
                                     damage_status=damaged)
                self.inventoried_items.append(item)
        return InventoryItems.inventoried_items

    # Function for PriceList.csv
    def price_csv(self):
        with open('PriceList.csv', newline='') as csv_price:
            csv_price = csv.reader(csv_price)
            for row in csv_price:
                # Identifies the item serial number with find_serial function
                item = self.find_serial(row[0])
                # Identifies the item price
                item.price = row[1]

    # Function for finding the serial number
    def find_serial(self, serial_num):
        for item in self.inventoried_items:
            if item.serial_num == serial_num:
                return item

    # Function for ServiceDatesList.csv
    def service_csv(self):
        with open('ServiceDatesList.csv', newline='') as csv_service:
            csv_service = csv.reader(csv_service)
            for row in csv_service:
                # Identifies item serial number with find_serial function
                item = self.find_serial(row[0])
                # Identifies the item service date
                item.service_date = row[1]

    # Creates the DamagedInventory.csv file, holds damaged items
    def damaged_list(self):
        # Creates a new file, or updates an existing file
        f = open("DamagedInventory.csv", "w")
        # Empty list as sentinel value
        damaged_items = []
        for i in self.inventoried_items:
            # Puts damaged items into damaged_items list
            if i.damage_status:
                damaged_items.append(i)
        # Sorts the items in the csv by price, descending
        sorted2 = sorted(damaged_items, key=lambda x: int(x.price), reverse=True)
        for item in sorted2:
            # Adds items into output through damaged_item_price function
            f.write(self.damaged_item_print(item))
        # Closes file
        f.close()

    # Function for outputting damaged items in required format per instructions
    @staticmethod
    def damaged_item_print(item: InventoryItem):
        return item.serial_num + "," + item.manufacturer + "," + item.product_type + "," + str(item.price) + "," + \
               item.service_date + "\n"

    # Creates the FullInventory.csv file, holds the entire inventory
    def full_list(self):
        f = open("FullInventory.csv", "w")
        # Sorts items in the csv alphabetically by manufacturer, descending
        sorted_items = sorted(inventory.inventoried_items, key=lambda x: x.manufacturer, reverse=False)
        for item in sorted_items:
            # Adds items to output through full_item_print function
            f.write(self.full_item_print(item))
        # Closes file
        f.close()

    # Print function for the FullInventory.csv
    @staticmethod
    def full_item_print(i: InventoryItem):
        # Sentinel value for damage status
        damaged = str()
        if i.damage_status:
            # Changes value for damaged status if the damage status=True
            damaged = "damaged"
        # Outputs the full inventory per instructions
        return "{},{},{},{},{},{}\n".format(i.serial_num, i.manufacturer, i.product_type, str(i.price),
                                            i.service_date, damaged)

    # This function creates inventory files for each type of product in the full inventory
    def type_csv(self):
        # Creates empty set to store product types
        type_set = set()
        for i in self.inventoried_items:
            # Adds each type of product into the set
            type_set.add(i.product_type)
        for item_type in type_set:
            # Creates a file for each product type, capitalizing the first letter of the product type
            f = open(item_type.capitalize() + "Inventory.csv", "w")
            item_types = []
            for i in self.inventoried_items:
                if i.product_type == item_type:
                    item_types.append(i)
            # Sorts items by serial number, ascending
            sorted_items = sorted(item_types, key=lambda x: int(x.serial_num), reverse=False)
            for item in sorted_items:
                # Adds items to output through type_item_print function
                f.write(self.type_item_print(item))
            # Closes file
            f.close()

    # Print function for [type]Inventory.csv
    @staticmethod
    def type_item_print(item: InventoryItem):
        # Sentinel value for damage status
        damaged = str()
        # Changes status to "damaged" if damage_status=True
        if item.damage_status:
            damaged = "damaged"
        # Outputs item information per instructions
        return "{},{},{},{},{}\n".format(item.serial_num, item.manufacturer, str(item.price),
                                         item.service_date, damaged)

    # Function for comparing dates
    @staticmethod
    def is_service_date_before_today(item: InventoryItem):
        # Finds the current date
        today = date.today()
        # Sets format for date
        month, day, year = map(int, item.service_date.split('/'))
        # Service date
        date1 = date(year, month, day)
        # Determines if date has passed or not
        return date1 <= today

    # Converts datetime into milliseconds for comparing dates
    @staticmethod
    def time_in_milli(item: InventoryItem):
        # Formats date
        month, day, year = map(int, item.service_date.split('/'))
        date1 = datetime(year, month, day)
        # Returns datetime in milliseconds
        return date1.timestamp()

    # Function for adding past dates into csv file
    def call_date(self):
        # Default empty list to add dates to
        past_dates = []
        for i in self.inventoried_items:
            # Uses is_service_date_before_today function to append dates into list
            if self.is_service_date_before_today(i):
                past_dates.append(i)
        # Creates csv for items that have been serviced
        f = open("PastServiceDateInventory.csv", "w")
        # Sorts items by date, from most recent to oldest
        sorted_items = sorted(past_dates, key=lambda x: self.time_in_milli(x), reverse=True)
        for item in sorted_items:
            # Uses full_item_print function to output items, as it's the same format
            f.write(self.full_item_print(item))
        # Closes file
        f.close()


# Calls the various functions to read and create files per instruction
inventory = InventoryItems()
inventory.damaged_list()
inventory.full_list()
inventory.type_csv()
inventory.call_date()
