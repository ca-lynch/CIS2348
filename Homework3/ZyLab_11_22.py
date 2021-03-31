# Cody Lynch
# 1954220

# Gets a string from the user
user_input = input()

# Creates a list by splitting the users string into individual words
words = user_input.split()

# For loop counts the frequency for each word in the users string
for i in words:
    # Outputs the count for each word
    print(i, words.count(i))
