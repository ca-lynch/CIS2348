# Cody Lynch
# 1954220

# Gets an integer from user
user_num = int(input("Enter integer:\n"))
# Squares users number
num_squared = user_num * user_num
# Cubes users number
num_cubed = user_num * user_num * user_num
# Outputs users chosen integer
print("You entered: {}".format(user_num))
# Outputs users integer squared
print("{} squared is {}".format(user_num, num_squared))
# Outputs users integer cubed
print("And {} cubed is {} !!".format(user_num, num_cubed))
# Gets a second number from user
user_num2 = int(input("Enter another integer:\n"))
# Prints the sum of the integers
print("{} + {} is {}".format(user_num, user_num2, user_num + user_num2))
# Prints the product of the integers
print("{} * {} is {}".format(user_num, user_num2, user_num * user_num2))
