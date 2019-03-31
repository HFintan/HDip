# Problem 7
# Returns the square root of a number to a specified
# number of decimals

# Used for rounding
# https://docs.python.org/3/tutorial/floatingpoint.html

import math

while True:
# FH - removed this afterwards when I realised floats were allowed.
# Also, was using .sqrt, but it seems that was not desired, so I went
# with ^0.5 instead.
#    try:
#        your_number = int(input("Please enter an integer greater than 1:"))
#    except ValueError:
#        print("You're not going to get very far with that. Please enter a whole number greater than 1.")
#        continue
#    if your_number < 2:
#        print("Please a enter a whole number GREATER than 1.")
#    else:
#        break
    try: 
        your_number = float(input("Please enter a number:"))
    except ValueError:
        print("A NUMBER, please!")
    else:
        break

while True:
    try:
        your_round = int(input("How many decimal places would you like to round to?"))
    except ValueError:
        print("Please enter a positive integer.")
        continue
    if your_round < 0:
        print("Please a enter a positive integer.")
    if your_round > 16:
        print("Eh... we'll see what we can do...")
        break
    else:
        break

#print("The square root of",your_number,"is approximately",round(float(math.sqrt(your_number)),your_round))
print("The square root of",your_number,"is approximately",round(float((your_number)**0.5),your_round))

