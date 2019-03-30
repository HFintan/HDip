# Problem 1
# sum of all integers from 0 to user-input n
# References: https://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response for Exception example

# Default true starts while loop, which prompts user for suitable input
while True:
    try:
        # asks user for integer input
        your_choice = int(input("Please enter a positive integer:"))
    except ValueError:
        # if input not an integer, returns user to prompt
        print("Try again. We're looking for a whole number greater than zero.")
        continue
    # if input an integer but negative, returns user to prompt
    if your_choice <0:
        print("Almost there! We're looking for a whole number GREATER than zero.")
    else:
        break

# Fomula uses fewer operations than adding up all the numbers.
print(int(your_choice*(your_choice+1)/2))
