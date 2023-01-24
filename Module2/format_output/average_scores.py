#Get first and Last Name
last_name = input("Enter your last name : ")
first_name = input("Enter your first name : ")
#Get Age
age = int(input("Enter your age: "))
#Get 3 scores
score1 = float(input("Enter your first score:"))
score2 = float(input("Enter your second score:"))
score3 = float(input("Enter your third score:"))
#Declare a Constant to represent the number of scores prompted
totalScores = 3
#Find average of the scores inputed
average = (score1 + score2 + score3) / totalScores
#Display the inputs correctly in the console after all information is inputed
print("{}, {} age: {} average grade: {:.2f}".format(last_name, first_name, age, average))

