# Cody Lynch
# 1954220

# Gets integers from user
user_input = input()

# Splits integers into individual values
tokens = user_input.split()

# Creates an empty list to be returned later
pos_nums = []

# For loop determines which numbers are positive
for token in tokens:
    if int(token) >= 0:
        # Adds number to input_data list if they are positive
        pos_nums.append(int(token))

# Sorts the numbers in the list from smallest to largest
pos_nums.sort()

# Prints the list of positive numbers
print(*pos_nums, end=' ')
