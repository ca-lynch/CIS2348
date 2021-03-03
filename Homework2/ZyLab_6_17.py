# Cody Lynch
# 1954220

# Gets a word from the user to be used as the password base
word = input()

# Creates an empty variable to become the new password
password = ''

# If statements that change targeted characters and store them to variable password
for i in word:
    if i == "i":
        password += "!"
    elif i == "a":
        password += "@"
    elif i == "m":
        password += "M"
    elif i == "B":
        password += "8"
    elif i == "o":
        password += "."
    else:
        password += i

# Concatenates "q*s" to the end of the password for extra strength
password = password + "q*s"

# Outputs the modified password
print(password)
