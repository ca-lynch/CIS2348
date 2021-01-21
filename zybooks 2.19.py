# Cody Lynch
# 1954220

paint_colors = {
   'red': 35,
   'blue': 25,
   'green': 23
}

wall_height = int(input('Enter wall height (feet):\n'))
wall_width = int(input('Enter wall width (feet):\n'))
wall_area = wall_height * wall_width
print('Wall area: {} square feet'.format(wall_area))
paint_needed = wall_area / 350
print("Paint needed: {:.2f} gallons".format(paint_needed))
cans_needed = round(paint_needed)
print("Cans needed: {} can(s)".format(cans_needed))

desired_color = (input("\nChoose a color to paint the wall:"))
print("\nCost of purchasing {} paint: ${}".format(desired_color, paint_colors[desired_color] * cans_needed))
