#117 Create a simple maths quiz that will ask the user for their name and then generate two random questions.
#Store their name, the questions they were asked, their answers and their final score in a .csv file.
#Whenever the program is run it should add to the .csv file and not overwrite anything.
import csv
import random

def quizmath():
    
    file = open("Math.csv","w")

    name = input('Enter your name: ')
    questions = ['1 + 1','2 + 2','3 + 5']
    score = 0
    print('Answer the next questions')

    for i in range(2):
        q = random.choice(questions)
        print(q)
        answer = int(input('Write your answer: '))
        if questions.index(q) == 0 and answer == 2:
            score += 1
        elif questions.index(q) == 1 and answer == 4:
            score += 1
        elif questions.index(q) == 2 and answer == 8:
            score += 1
        else:
            score += 0

        file.write(name +","+ q +","+str( answer)+"\n")
    file.write('Final Score'+" "+str(score))
    file.close()
    
    
            


quizmath()

