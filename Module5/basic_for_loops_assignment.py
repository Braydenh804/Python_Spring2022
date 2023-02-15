'''
This code prints a list of floats to the console and prints all of the odd numbers from 99 descending to 33
'''
floats = [41.24, 124.51, 98.12, 12.87] # List of floats
for w in floats:
    print(float(w)) # For loop that prints every float in the list

for i in range(99, 32, -2):
    print(i) # This loop starts at 99 and goes down to 33, with a step size of -2 which allow it to skip all of the
    # even numbers
