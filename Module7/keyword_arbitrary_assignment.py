def average_scores(*args, **kwargs):
    '''
    :param args: These are the numbers pasted in to calculate a new average gpa
    :param kwargs: These are the persons info like name, old gpa and course they are taking
    :return: Returns a string that displays there new gpa
    '''
    # Use *args for average calculation
    average_score = sum(args) / len(args)
    gpa = average_score
    # Print Keyword Values
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))
    return "new_gpa == " + str(average_score)


if __name__ == '__main__':
    print(average_scores(4, 3, 2, 4, name='Brayden', old_gpa=3, course='Python'))
    print(average_scores(4, 3, 4, 4, 1, name='Bob', old_gpa=2.5, course='Composition 1'))
    print(average_scores(4, 3, 2, 4, 1, 3, 2, name='John', old_gpa=1.75, course='Calculus 1'))