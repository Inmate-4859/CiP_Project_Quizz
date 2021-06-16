import json
import datetime
import random

# Converts list into dictionary setting, for each pair of elements,
# the first one as the key and the second one as the value
# that is what the third argument in the range does


def Convert(lst):
    res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
    return res_dct


def Test():
    global fileName, correctAnswers, totalQuestions, gradePercentage
    # Imports the data from the file of your choice and assigns it
    # to a the variable 'lst' which is going to be a list
    fileName = input('File name: ')
    try:
        with open(fileName) as json_file:
            lst = json.load(json_file)
    except:
        print('Not a valid test file. Check upper and lower case letters and do not forget to add the .txt at the end.')
        Test()
        gradeSaving()
        anotherOne()

    # Defining the dictionary as a result of the Convert function

    newDict = Convert(lst)

    # Defining the variables for the data we want to return after the test
    errors = []
    totalQuestions = 0
    correctAnswers = 0

    # Loop 1 that makes the questions, adds to the variables before for each
    # loop. To 'correctAnswers' if it is correct, copies the answer to [errors] if
    # it was incorrect, and finally one + to 'totalQuestions' for each iteration.
    # Asks questions in random order, to avoid memorising a pattern and not the
    # correct answers independently.

    dictKeys = list(newDict.keys())
    randomDictKeys = random.sample(dictKeys, len(dictKeys))

    for x in randomDictKeys:
        totalQuestions += 1
        res = input(f'Q {totalQuestions}: {x}--> ')
        if res.casefold() == newDict.get(x):
            correctAnswers += 1
        else:
            errors.append(f'{x} --> {newDict.get(x)}. Your answer was: {res}')

    # Prints the number of correct answers and gives the total number of questions,
    # giving a grade in percentage

    print(' ')
    print('---------------------------------------------------------------')
    print('---------------------------------------------------------------')
    print(' ')
    print(f'You had {correctAnswers} correct answers out of {totalQuestions}')
    gradePercentage = int(correctAnswers)*100/int(totalQuestions)
    print(f'That is {gradePercentage} % of the total marks')

    # Prints the wrong answers, if any, and the right answer as per what is set
    # on the else statement of loop 1

    if len(errors) >= 1:
        print('Your mistakes were: \n')
        for x in errors:
            print(f'{x}\n')
    else:
        print(f'Congratulations, you have scored a perfect test!')


# Saves results to a .txt file, also including the name of the test, date and time.

def gradeSaving():
    saveGradesCheck = input('Would you like to save your results? Y/N: ')
    if saveGradesCheck.casefold() == 'y':
        endingTime = str(datetime.datetime.now())[:-7]
        global finalGrade, fileNameMod
        fileNameMod = fileName[:-5]
        finalGrade = f'{fileNameMod.capitalize()} on {endingTime} was {correctAnswers} out of {totalQuestions}, or {gradePercentage} %'
        with open('Grades.txt', mode='a') as textGrades:
            textGrades.write('\n')
            textGrades.write(finalGrade)
        pass
    else:
        pass


# Checks if the user wants to take another test.

def anotherOne():
    anotherTest = input('Would you like to take another test? Y/N: ')

    while anotherTest.casefold() == 'y':
        Test()
        gradeSaving()
        anotherOne()
    else:
        pass


# Functions running

Test()
gradeSaving()
anotherOne()

input("\n\nAll done! Press enter key to exit.")
exit()
