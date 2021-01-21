# Cody Lynch
# 1954220

# Gets the current date from the user
current_date = input("Enter today's date (mm/dd/yyyy):\n")
# Gets the users DOB
user_birthday = input("Enter your birthday (mm/dd/yyyy):\n")
# Splits the dates into months days and years to make comparing dates easier
date_numbers = current_date.split("/")
birthday_numbers = user_birthday.split("/")
# Stores the values into the month day and year for the current date
date_month = int(date_numbers[0])
date_day = int(date_numbers[1])
date_year = int(date_numbers[2])
# Stores the values into the month day and year for the users birthday
birthday_month = int(birthday_numbers[0])
birthday_day = int(birthday_numbers[1])
birthday_year = int(birthday_numbers[2])
# First calculation based off of year only
base_years = date_year - birthday_year
# Final calculation based off of month and day, also checks if it's users birthday
if date_month < birthday_month:
    base_years = base_years - 1
elif date_month >= birthday_month and date_day < birthday_day:
    base_years = base_years - 1
elif current_date[0:5] == user_birthday[0:5]:
    print("Happy Birthday!")

# Outputs all values, and calculates age
print("Birthday Calculator")
print("Current Day")
print("Month: {}".format(date_month))
print("Day: {}".format(date_day))
print("Year: {}".format(date_year))
print("Birthday")
print("Month: {}".format(birthday_month))
print("Day: {}".format(birthday_day))
print("Year: {}".format(birthday_year))
print("You are {} years old.".format(base_years))
