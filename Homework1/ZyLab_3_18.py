# Cody Lynch
# 1954220

# Creates dictionary to match paint colors to prices
paint_colors = {
   'red': 35,
   'blue': 25,
   'green': 23
}
# Gets wall height and width from user
wall_height = int(input('Enter wall height (feet):\n'))
wall_width = int(input('Enter wall width (feet):\n'))
# Calculates then outputs the walls area in square feet
wall_area = wall_height * wall_width
print('Wall area: {} square feet'.format(wall_area))
# Calculates then outputs the amount of paint needed in gallons
paint_needed = wall_area / 350
print("Paint needed: {:.2f} gallons".format(paint_needed))
# Calculates then outputs the amount of paint needed in cans
cans_needed = round(paint_needed)
print("Cans needed: {} can(s)".format(cans_needed))
# Gets desired color from user then outputs the cost for the paint
desired_color = (input("\nChoose a color to paint the wall:"))
print("\nCost of purchasing {} paint: ${}".format(desired_color, paint_colors[desired_color] * cans_needed))
