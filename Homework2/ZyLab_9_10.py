# Cody Lynch
# 1954220

# Imports comma separated value module
import csv

# Gets file name from user
fileName = input()

# Creates empty dictionary
wordsFrequency = {}

# Counts the frequency of words
with open(fileName, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        for word in row:
            if word not in wordsFrequency.keys():
                wordsFrequency[word] = 1
            else:
                wordsFrequency[word] += 1

# Prints the word frequency
for key in wordsFrequency.keys():
    print(key + " " + str(wordsFrequency[key]))
