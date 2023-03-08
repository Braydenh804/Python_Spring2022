def get_test_scores():
    '''
    Adds users score inputs into a dictionary with a unique keyword then calls a function to find the average score of
    the values stored in the dictionary.
    '''
    scores_dict = dict()  # Dictionary declared
    num = 1  # A number that is put on the end of the keyword of score, so the keywords can be named score1 score2 ect.
    key = "score" + str(num)  # Adding the number to the string that will be saved as the first keyword
    i = False  # Loop Condition
    while not i:  # Loop that does not end until I = true
        try:
            dict_input = int(input("Enter your score between 1 and 100 (-1 to exit): "))  # User inputs a value
            if 1 <= dict_input <= 100:  # Checks if the value is going to be stored in the list
                scores_dict.update({key: dict_input})  # Adds the valid number to the dictionary
                num = num + 1  # Add 1 so the keyword is different on the next loop
                print(str(dict_input) + " has been added to the dictionary under keyword " + key)
                # Confirms there input is going to be in the list
                key = "score" + str(num)
            elif dict_input == -1:  # If value is valid above but is equal to -1 end loop
                print("Thank you for entering your scores")
                print(scores_dict)
                break  # Forces the loop to end once -1 is entered
            else:
                raise ValueError('Bad Input')  # If value doesn't fit the criterion raise error to restart code
        except ValueError:
            print("Please input a valid number")  # Before code restarts inform user the input was invalid
    average_scores(num, scores_dict)


def average_scores(num, dictionary):
    '''
    :param num: This value is passed as when you subtract 2 you will have the number of scores that were entered into
    the dictionary which is used to compile the numbers into a list, so I could get the sum.
    :param dictionary: This value is the dictionary created in the last function which hold the values that we need to
    average.
    '''
    score_list = []  # Defines a list to store the score into, so they can be summed
    i = 0  # A value used to search the dictionary and store the values in the above list
    while i < num-2:  # Loop until all values are stored
        key_list = list(dictionary.keys())
        key = key_list[i]
        score = dictionary.get(key)
        score_list.append(score)
        i = i + 1
    average_score = sum(score_list) / len(score_list)  # Calculate the average of the values stored in the score_list
    print("Your Average Score is: " + str(average_score))  # Print to console what the average score is


if __name__ == '__main__':
    get_test_scores()
