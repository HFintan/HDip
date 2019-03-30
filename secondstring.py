# Q6
# Program takes an input string and outputs every nth word
# starting with a user-inputted offset

# Used for info on split
# http://www.pitt.edu/~naraehan/python3/split_join.html

while True:
    try:
        your_increment = int(input("Please enter an integer greater than 0 for the increment:"))
    except ValueError:
        print("You're not going to get very far with that. Please enter a whole number greater than 0.")
        continue
    if your_increment < 1:
        print("Please enter a whole number GREATER than 0.")
    else:
        break

while True:
    try:
        your_offset = int(input("Please enter a non-negative integer for the offset:"))
    except ValueError:
        print("You're not going to get very far with that. Please enter a non-negative integer:")
        continue
    if your_offset < 0:
        print("Please enter a non-negative integer:")
    else:
        break

while True:
    try:
        your_string = str(input("Please enter a string:\n"))
    except ValueError:
        print("Please try again.")
        continue
    else:
        split_string = your_string.split()
        for i in range(your_offset,len(split_string),your_increment):
            print(split_string[i], end=' ')
        break
