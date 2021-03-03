# Cody Lynch
# 1954220

# Assigns first set of values values
a = int(input())
b = int(input())
c = int(input())


# Assigns second set of values
d = int(input())
e = int(input())
f = int(input())

# Creates equations
y = (c - (a * f / d)) / (b - (e * a / d))
x = ((c / a) - (b * y / a))

# Sets parameters and gives rounded output
if -10 > round(x) or 10 < round(x):
    print("There is no solution")
elif -10 > round(y) or 10 < round(y):
    print("No solution")
else:
    print(round(x), (round(y)))
