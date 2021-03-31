# Cody Lynch
# 1954220

# Creates an empty dictionary to begin building team
team_dict = {}

# Sets default player number to 1 to begin building team
player_number = 1

# For loop creates an initial list of 5 players
for i in range(1, 6):
    # Gets a jersey number from user
    jersey_number = int(input('Enter player {}\'s jersey number:\n'.format(i)))
    # Gets a rating from user
    rating = int(input('Enter player {}\'s rating:\n'.format(i)))
    print()
    # Sets limits for valid entries
    # Jersey number must be between 0 and 99 and rating must be between 0 and 9
    if jersey_number < 0 or jersey_number > 99 or rating < 0 or rating > 9:
        print('invalid entry')
        break
    else:
        team_dict[jersey_number] = rating

# Prints header for roster
print("ROSTER")
# Prints the team roster in ascending order by jersey number
for jersey_number, rating in sorted(team_dict.items()):
    print("Jersey number: %d, Rating: %d" % (jersey_number, rating))

# Sentinel value for menu option
option = ''

# Creates an interactive menu for the user
# While loop initiates as long as option value is not q or Q
while option.upper() != 'Q':
    print('\nMENU\n'
          'a - Add player\n'
          'd - Remove player\n'
          'u - Update player rating\n'
          'r - Output players above a rating\n'
          'o - Output roster\n'
          'q - Quit\n')

    # Gets command from user
    option = input('Choose an option:\n')

    # If else statements determine which option will initiate
    # Adds a new player to the dictionary
    if option == 'a':
        jersey_number = int(input('Enter a new player\'s jersey number:\n'.format(player_number)))
        rating = int(input('Enter the players\'s rating:\n'.format(player_number)))
        team_dict[jersey_number] = rating

    # Deletes an existing player from the dictionary by jersey number
    elif option == 'd':
        jersey_number = int(input('Enter a jersey number:\n'))
        if jersey_number in team_dict.keys():
            del team_dict[jersey_number]

    # Updates an existing players rating
    elif option == 'u':
        jersey_number = int(input('Enter a jersey number:\n'))
        if jersey_number in team_dict.keys():
            rating = int(input('Enter a new rating for player:\n'))
            team_dict[jersey_number] = rating

    # Outputs players who have a rating above user input
    elif option == 'r':
        rating_input = int(input('Enter a rating:\n'))
        print('ABOVE {}'.format(rating_input))
        for jersey_number, rating in sorted(team_dict.items()):
            if rating > rating_input:
                print("Jersey number: %d, Rating: %d" % (jersey_number, rating))

    # Prints the current roster
    elif option == 'o':
        print("ROSTER")
        for jersey_number, rating in sorted(team_dict.items()):
            print("Jersey number: %d, Rating: %d" % (jersey_number, rating))
