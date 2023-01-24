# Allows user to input age and assigns it to the userAge variable
userAge = input('Enter your age here:')
# Adding a year variable so I can subtract there age from the year to find there birth year
year = 2023
# Since I am not asking for the month and date I cant be 100% sure what year so ill subtract one so it will give 2
# different birth years so that their birth year will be for sure displayed
print("You were born in either", year - int(userAge)-1, "or", year - int(userAge))