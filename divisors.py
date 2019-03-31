# Question 3
# Takes as input an upper and lower bound integer, and returns those
# integers between them which are divisible by 6 but not 12
# Takes optional range, rather than range in problem sheet, so
# I could compare times. 

# used 
# https://pythonhow.com/measure-execution-time-python-code/ 
# to check how to time things in python
# https://stackoverflow.com/questions/39801441/can-i-use-a-variable-inside-of-an-input-statement
# to see how to put variable in print string

import time

while True:
    try:
        lower_bound=int(input("Please input a non-negative integer for the lower bound:"))
    except ValueError:
        print("Please try again. We want a whole number, greater than or equal to 0.")
        continue
    if lower_bound < 0:
        print("Please try again. We want a whole number, GREATER THAN OR EQUAL TO 0.")
    else:
        break

while True:
    try:
        upper_bound=int(input("Please input a non-negative integer greater than {} for the upper bound:".format(lower_bound)))
    except ValueError:
        print("Please try again. We want a whole number, greater than ", lower_bound)
        continue
    if not (upper_bound > lower_bound):
        print("Please try again. Your upper bound must be GREATER than your lower bound.")
    else:
        break

start=time.time()

# Method 1 - checks whether each number divides by 6
# and not by 12
# Noticeably slower than Method 2
"""
for i in range(lower_bound, upper_bound):
    if i % 6 == 0 and not i % 12 == 0:
        print(i, end = ', ')
"""
# End Method 1

# Method 2 - finds lowest n >= lower bound which divides
# by 6, and adds 12 recursively
# There isn't a big difference between Methods 2A and 2B
while not lower_bound % 6 == 0 or lower_bound % 12 == 0:
    lower_bound = lower_bound+1

# Method 2A (uses while loop with increment)
"""
while lower_bound <= upper_bound:
    print(lower_bound, end =', ')
    lower_bound = lower_bound+12
"""
# End Method 2A

#Method 2B (uses the increment from the range function)
for i in range(lower_bound, upper_bound, 12):
    print(i, end = '\n')
# End Method 2B
# End Method 2

end = time.time()

print("\n time = ", end-start)

