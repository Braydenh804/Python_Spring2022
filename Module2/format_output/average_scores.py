# Get first and Last Name
last_name = input("Enter your last name : ")
first_name = input("Enter your first name : ")
# Get Age while prompting a non-negative input value
i = False
while not i:
    try:
        age = int(input("Enter your age: "))
        age_as_int = int(age)
        if (age_as_int >= 0):
            i = True
        else:
            raise ValueError('Bad Input')
    except:
        print("Please input a valid number")
# Get 3 scores while prompting a non-negative input value
i = False
while not i:
    try:
        score1 = float(input("Enter your first score:"))
        score1_as_int = int(score1)
        if (score1_as_int >= 0):
            i = True
        else:
            raise ValueError('Bad Input')
    except:
        print("Please input a valid number")

i = False
while not i:
    try:
        score2 = float(input("Enter your second score:"))
        score2_as_int = int(score2)
        if (score2_as_int >= 0):
            i = True
        else:
            raise ValueError('Bad Input')
    except:
        print("Please input a valid number")

i = False
while not i:
    try:
        score3 = float(input("Enter your third score:"))
        score3_as_int = int(score3)
        if (score3_as_int >= 0):
            i = True
        else:
            raise ValueError('Bad Input')
    except:
        print("Please input a valid number")

# Declare a Constant to represent the number of scores prompted
totalScores = 3
# Find average of the scores inputed
average = (score1 + score2 + score3) / totalScores
# Display the inputs correctly in the console after all information is inputed
print("{}, {} age: {} average grade: {:.2f}".format(last_name, first_name, age, average))
