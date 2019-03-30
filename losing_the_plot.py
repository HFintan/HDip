# Problem 10

# Ask user for range for x
while True:
    try:
        lower_value = int(input("What range of values for the x-axis? Please enter the lowest value for x:"))
    except ValueError:
        print("Computer says no. We are looking for a number.")
        continue
    else:
        break

while True:
    try:
        upper_value = int(input("Please enter the highest value for x:"))
    except ValueError:
        print("Nope. We are looking for a number - the highest value you want for x.")
        continue
    if lower_value > upper_value:
        print("Your upper value must be greater than your lower value, surprisingly. Try again. What upper value for x would you like?")
        continue
    else:
        break

import matplotlib.pyplot as plt

linear=[]
squared=[]
tutu_power=[]

# added the +1 because when someone asks for a 0,5 range, they want to see the 5...
# normal people, at least.
for i in range(lower_value, upper_value+1):
    linear.append(i)
    squared.append(i**2)
    tutu_power.append(2**i)

min_y_val =min(min(i) for i in [linear,squared,tutu_power]) 
max_y_val =max(max(i) for i in [linear,squared,tutu_power]) 


plt.plot(range(lower_value,upper_value+1),linear, label='x')
plt.plot(range(lower_value,upper_value+1),squared, label='x^2')
plt.plot(range(lower_value,upper_value+1),tutu_power, label='2^x')
plt.axis([lower_value,upper_value,min_y_val,max_y_val])
legend = plt.legend(loc='upper center', fontsize='large')

plt.show()


