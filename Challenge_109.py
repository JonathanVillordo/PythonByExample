#109

def selectop():

    print('1) Create a new file\n2) Display the file\n3)nAdd a new item to the file\nMake a selection 1, 2 or 3: ')
    choice = int( input("Select an option: "))
    if choice == 1:
        subject = input('Enter a Subject: ')
        file = open('Subject.txt','w+')
        file.write(subject+'\n')
        file.close()
    elif choice == 2:
        file = open('Subject.txt','r')
        print(file.read())
    elif choice == 3:
        subject = input('Enter a Subject: ')
        file = open('Subject.txt','a')
        file.write(subject+'\n')
        file.close()
    else:
        print('Wrong choice')

selectop()
