# Cody Lynch
# 1954220

# Defines function to get change converter
def exact_change(user_total):
    if user_total <= 0:
        print("no change")
        return 0, 0, 0, 0, 0
    else:
        dollars = user_total // 100
        quarters = (user_total % 100) // 25
        dimes = (user_total % 100 % 25) // 10
        nickels = (user_total % 100 % 25 % 10) // 5
        pennies = user_total % 100 % 25 % 10 % 5
        return dollars, quarters, dimes, nickels, pennies


if __name__ == '__main__':
    input_val = int(input())  # Gets amount from user
    num_dollars, num_quarters, num_dimes, num_nickels, num_pennies = exact_change(input_val)  # Calls function

# If statements to create output
    if num_dollars == 1:
        print("1 dollar")
    elif num_dollars > 1:
        print(str(num_dollars) + " dollars")
    if num_quarters == 1:
        print("1 quarter")
    elif num_quarters > 1:
        print(str(num_quarters) + " quarters")
    if num_dimes == 1:
        print("1 dime")
    elif num_dimes > 1:
        print(str(num_dimes) + " dimes")
    if num_nickels == 1:
        print("1 nickel")
    elif num_nickels > 1:
        print(str(num_nickels)+" nickels")
    if num_pennies == 1:
        print("1 penny")
    elif num_pennies > 1:
        print(str(num_pennies)+" pennys")
