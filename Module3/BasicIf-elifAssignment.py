# Ask the customer if there interested in the free trial of the product
print("Hello would you like to sign up for Programmer's Toolkit To get started we have a Free Trial for 7 days if "
      "your interested")
# Make an array to hold the levels of subscription
SubscriptionPackages = ["Silver: 40$ A Month", "Gold: 50$ A Month", "Platinum: 60$ A Month"]
# Allow user to type "yes" or "no" regardless of format and store it as a variable
FreeTrial = input("Type yes if you would like to start the free trail or no if you dont:").lower()
# Remove all whitespaces from input
FreeTrial = FreeTrial.strip()
# Convert string to all lowercase
FreeTrial = FreeTrial.lower()
# Declare a variable that will be true or false whether the free trial will begin or not
StartFreeTrial = False
# Find out if the input was Yes or No or invalid
i = False
while not i:
    if FreeTrial == "yes":
        StartFreeTrial = True
        i = True
    elif FreeTrial == "no":
        StartFreeTrial = False
        i = True
    else:
        FreeTrial = input("Invalid input please type yes or no:")
        # Through testing, I found I needed to reformat the variable inside the loop because it wouldnt get formated by the original code
        FreeTrial = FreeTrial.lower()
        FreeTrial = FreeTrial.strip()
# Make an array to hold the levels of subscription you can upgrade to
SubscriptionPackages = ["Silver: 40$ A Month", "Gold: 50$ A Month", "Platinum: 60$ A Month"]
# Thank the user for signing up and give User the option to upgrade to a higher package after there Free Trial is over
if StartFreeTrial == True:
    print("Thanks for signing up for Programmer's Toolkit your free trial ends in 7 days and after that you will be "
          "charged 30$ for the Bronze subscription or you can choose to upgrade to the following packages:")
    for i in SubscriptionPackages:
        print(i)
    UpgradedPackage = input("Type what package you would like to upgrade to or type no if you are not interested in upgrading:")
    # Remove all whitespaces from input
    UpgradedPackage = UpgradedPackage.strip()
    # Convert string to all lowercase
    UpgradedPackage = UpgradedPackage.capitalize()
    # Find what package they are upgrading and display the price
    i = False
    while not i:
        if UpgradedPackage == "No":
            print("Thanks for your input we hope you enjoy your Bronze package")
            i = True
        elif UpgradedPackage == "Silver":
            print("Thanks for upgrading to Silver you will now be charged 40$ in 7 days")
            i = True
        elif UpgradedPackage == "Gold":
            print("Thanks for upgrading to Gold you will now be charged 50$ in 7 days")
            i = True
        elif UpgradedPackage == "Platinum":
            print("Thanks for upgrading to Platinum you will now be charged 60$ in 7 days")
            i = True
        else:
            UpgradedPackage = input("Invalid Input Please Retype:")
            # Same as line 26 and 27 I needed to reformat them in the loop because the above code would not be run again
            UpgradedPackage = UpgradedPackage.strip()
            UpgradedPackage = UpgradedPackage.capitalize()
else:
    print("Thanks for taking a look if you ever become interested remember you can always cancel after your 7 day Free Trial")