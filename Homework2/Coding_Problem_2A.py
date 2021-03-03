# Cody Lynch
# 1954220

# Imports datetime module
import datetime

# Lists months for index reference
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November",
          "December"]

# Checks month and day to pass or reject
def date_acceptor(user_date):
    month_accepted = False
    day_accepted = False
    for month in months:
        if user_date.find(month) == 0:
            month_accepted = True
            break
    user_date_split = user_date.split()
    if len(user_date_split) > 1:
        get_user_day = user_date_split[1]
        if get_user_day.find(",") != -1:
            day_accepted = True
    return month_accepted & day_accepted


def date_parser(user_date):
    if date_acceptor(user_date):
        # Finds month in input and converts it to an integer, or rejects improper input
        user_month = 0
        for index in range(len(months)):
            if user_date.find(months[index]) == 0:
                user_month = index + 1
                break
        if user_month > 0:
            # Gets the current date and formats it
            get_current_date = datetime.date.today()
            # Converts today's date into individual values
            current_month = int(get_current_date.month)
            current_day = int(get_current_date.day)
            current_year = int(get_current_date.year)
            # Converts date into individual values
            user_date_split = user_date.split()
            get_user_day = user_date_split[1]
            user_day = int(get_user_day[:-1])
            user_year = int(user_date_split[2])
            # Sets the users date to the correct format
            user_date_final = "{}/{}/{}".format(user_month, user_day, user_year)
            # Prints the users date if the date is not in the future
            if user_year < current_year:
                return user_date_final
            elif user_year <= current_year and user_month < current_month:
                return user_date_final
            elif user_year <= current_year and user_month <= current_month and user_day <= current_day:
                return user_date_final

# Exits if input is -1, or sends output
def input_from_user(user_input):
    if user_input == "-1":
        exit(-1)
    else:
        output = date_parser(user_input)
        if output is not None:
            print(date_parser(user_input))
        input_from_user(input())

# Calls function for user input
input_from_user(input())
