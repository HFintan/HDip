# Q5
# This script checks whether a number is prime by attempting to
# divide it by every number less than its square root (plus one
# for convenience). If the number is prime, it adds it to another
# file containing a list of the primes you have thus far discovered.

# Used https://stackoverflow.com/questions/4706499/how-do-you-append-to-a-file-in-python# for appending to a file

import math
import time

while True:
    try:
        your_number = int(input("Please enter an integer greater than 1:"))
    except ValueError:
        print("You're not going to get very far with that. Please enter a whole number greater than 1.")
        continue
    if your_number < 2:
        print("Please a enter a whole number GREATER than 1.")
    else:
        break

square_root=int(math.sqrt(your_number))
for i in range(2,square_root+1):
    if your_number % i == 0:
        print ("Your number is not prime, as it is divisible by", i)
        break
else:
    print("\nYour number appears to be prime!\n")
    time.sleep(1)
    print("Let's add it to our big list of primes.\n")
    time.sleep(1)
    try:
        primes_list=open('My-first-book-of-primes.txt', "r")
    except FileNotFoundError:
        print("Ooh, it looks like",your_number,"is your very first prime! How exciting!")
        primes_list=open('My-first-book-of-primes.txt', "w")
        primes_list.write(f'{your_number}')
    else:
        for line in primes_list:
            if your_number == int(line):
                print("Hmm... seems we already have that one.")
                break
        else:
            primes_list=open('My-first-book-of-primes.txt', "a")
            primes_list.write(f'\n{your_number}')

