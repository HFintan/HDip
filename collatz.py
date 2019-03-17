# Q4 on problem sheet. 
# Collatz conjecture. If n/2 is not 0, n becomes 3*n+1
# Eventually this becomes 1. This function shows the steps and counts them.
# It also, if necessary, updates a file collatz_record.txt which stores
# the user's current record for maximum number of steps involved in 
# reaching 1.

# I left some time between the starting and ending this script, so I cannot
# remember all of the webpages I consulted trying to get the file reading/writing
# to work. And it seems "readlines" is generally undesirable, but I could not
# come up with another succinct way to read the entire line as an integer, rather
# than just the first character.

while True:
    try:
        your_number = int(input("Please enter an integer greater than 0:"))
    except ValueError:
        print("You're not going to get very far with that. Please enter a whole number greater than 0.")
        continue
    if your_number < 1:
        print("Please a enter a whole number GREATER than 0.")
    else:
        break

print("Your number is ", your_number, "and the steps on your Collatz journey are:")
step_count = 0

initial_number=your_number

while your_number != 1:
    if your_number % 2 == 0:
        your_number = int(your_number/2)
        print(your_number, end=' ')
        step_count = step_count+1
    else: 
        your_number = your_number*3+1
        print(your_number, end=' ')
        step_count = step_count+1
    continue

print("\nThat took", step_count, "steps.")

try:
    record_file=open('Collatz-record.txt', "r")
except FileNotFoundError:
    print("The file Collatz-record.txt does not appear to exist. This must be your first attempt. Congratulations on setting a new record!")
    record_file=open("Collatz-record.txt", "w")
    record_file.write(f'{initial_number}\n{step_count}')  
else:
    record_file_lines=record_file.readlines()
    held_by = int(record_file_lines[0])
    old_record=int(record_file_lines[1])
    if old_record < step_count:
        print("Wow! A new record! The old record for the greatest number of steps was", old_record, "steps, held by", held_by, "but you've beaten it, with",initial_number, "which takes a whopping", step_count, "steps!")        
        record_file=open('Collatz-record.txt', "w")
        record_file.write(f'{initial_number}\n{step_count}')
    else: 
        print("The current record is", old_record, "steps, held by", held_by)
    record_file.close()




        
