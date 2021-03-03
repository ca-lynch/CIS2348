# Cody Lynch
# 1954220

# Gets user string
user_string = str(input())

# Removes spaces
original = user_string.replace(' ', '')

# Reverses string
backwards = user_string.replace(' ', '')[::-1]

# Determines if the string is a palindrome
if original == backwards:
    print(user_string, 'is a palindrome')
else:
    print(user_string, 'is not a palindrome')
