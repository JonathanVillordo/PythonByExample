#072 Create a list of six school subjects. Ask the user which of these subjects they don’t like.
#Delete the subject they have chosen from the list before you display the list again.

def subjects():

    subjects = ['Mathematics','Spanish','Art','Geography','Music','Natural History']
    print(subjects)
    answer = input("Enter the subject you don't like :")
    subjects.remove(answer)
    print(subjects)

subjects()
