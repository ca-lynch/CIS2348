# Cody Lynch
# 1954220

# Gets initial list of ingredients and amounts
lemon_juice_cups = float(input('Enter amount of lemon juice (in cups):\n'))
water_cups = float(input("Enter amount of water (in cups):\n"))
agave_cups = float(input("Enter amount of agave nectar (in cups):\n"))
servings = float(input("How many servings does this make?\n"))

# Outputs ingredients and amounts
print("\nLemonade ingredients - yields", "{:.2f}".format(servings), "servings")
print("{:.2f}".format(lemon_juice_cups), "cup(s) lemon juice")
print("{:.2f}".format(water_cups), "cup(s) water")
print("{:.2f}".format(agave_cups), "cup(s) agave nectar\n")

# Gets users desired amount of lemonade, and calculates amount of ingredients needed
desired_amount = float(input("How many servings would you like to make?\n"))
adjustment_number = desired_amount / servings
adjusted_lemon = lemon_juice_cups * adjustment_number
adjusted_water = water_cups * adjustment_number
adjusted_agave = agave_cups * adjustment_number

# Outputs amount of ingredients needed to make desired amount in cups
print("\nLemonade ingredients - yields", "{:.2f}".format(desired_amount), "servings")
print("{:.2f}".format(adjusted_lemon), "cup(s) lemon juice")
print("{:.2f}".format(adjusted_water), "cup(s) water")
print("{:.2f}".format(adjusted_agave), "cup(s) agave nectar\n")

# Converts ingredients amount from cups to gallons
lemon_gallon = adjusted_lemon / 16
water_gallon = adjusted_water / 16
agave_gallon = adjusted_agave / 16

# Outputs amount of ingredients needed in gallons
print("Lemonade ingredients - yields", "{:.2f}".format(desired_amount), "servings")
print("{:.2f}".format(lemon_gallon), "gallon(s) lemon juice")
print("{:.2f}".format(water_gallon), "gallon(s) water")
print("{:.2f}".format(agave_gallon), "gallon(s) agave nectar")
