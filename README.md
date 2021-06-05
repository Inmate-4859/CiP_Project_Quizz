# CiP_Project_Quizz


This is my final project for the 2021 iteration of Code in Place. 


It is a basic program that allows the user to create any number of quizzes of the 'question --> answer' kind so that first, the user creates a quizz with the questions and the 
correct answers, using 'createQuizz.py', which will create a JSON file for that quizz. Then, the user may create any other quizzes or start one of them using the 'Quizz.py' file.
In it, the user will be asked which quizz of the ones locally saved they want to take, and then the quizz will start.

'Quizz.py' will ask the user the questions that are in the JSON file, in random order, and give the user a result in x out of y questions correct and in percentage of correct 
answers. Then, the user will be asked if they want to save a log of that grade. If so, a 'Grades.txt' file will be created and all the future saved logs will go there as well.
The log will save the x out of y ratio and the percentage of correct answers, as well as the date, time and name of the quizz. 
