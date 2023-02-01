# declaring a MIN, MAX, and y variable
MAX = 10
MIN = 5
y = 11
# Check to see if y is above the MAX and display if it is or isn't
if y > MAX:
    print("y is greater than the MAX")
else:
    print("y isn't greater than the MAX")
# Check to see if y is below MIN
if y< MAX:
    print("y is less than the MIN")
else:
    print("y isn't less than the MIN")
# Declare an x variable
x = 11
# Run if statement to find if x is between the MIN and MAX but does not equal MAX nor MIN or if it isn't
if MIN < x < MAX:
    print("x is inbetween MIN and MAX but does not equal MAX nor MIN")
else:
    print("x isn't inbetween MIN and MAX and might equal either MAX or MIN")
# Run if statement to find if x is within MIN up to MAX but does not equal MAX or if it isn't
if MIN >= x < MAX:
    print("x is within MIN up to MAX but does not equal MAX")
else:
    print("x is not within MIN up to MAX but could equal MAX")
# Run if statement to find if x is above MIN up to and including MAX or if it isn't
if MIN < x <= MAX:
    print("x is above MIN up to and including MAX")
else:
    print("x is not above MIN up to and including MAX")
