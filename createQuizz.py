import json
qna = []

# naming the file containing the data
fileName = input('Name of the questionnaire : ') + '.json'


def addQuestion():
    # appends first questions and then answers, for the
    # conversion from list to dictionary to happen
    global q, a
    q = input('Question: ')
    if q == 'stop':
        exit()
    a = input('Answer: ')
    print(f'Last item: {q} -> {a} ')
    # goes back to the function if you tell it the equivalence of last item
    # if it is not correct, otherwise it writes the input in the txt file
    checkyCheck = input('Correct? Y/N: ')
    if checkyCheck.casefold() == 'y':
        qna.append(q)
        qna.append(a)
        with open(fileName, mode='w+') as textFile:
            # need json module to write lists
            # they won't have a name (be defined)
            json.dump(qna, textFile)
        pass
    else:
        print('Go back. ')
        addQuestion()


# actual function loop running
while True:
    addQuestion()

input("\n\nPress enter key to exit.")
exit("Done!")
