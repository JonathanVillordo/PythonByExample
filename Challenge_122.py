#122 file

def write_file():
    
    name = input('Enter your name: ')
    salary = int(input('Enter your salary: '))

    file = open('Salary.txt','w')
    file.write(name+' '+str(salary))
    file.close()

def print_file():

    file = open('Salary.txt','r')
    for i in file:
        print(i)

def main():

    option = 1

    while option in (1,2):
        option = int(input( '1) Add to file''\n'
                    '2) View all records' '\n'
                    '3) Quit program''\n\n'
                    'Enter an option: '
                  ))
        if option == 1:
            write_file()
        elif option == 2:
            print_file()
        elif option == 3:
            pass
        else:
            print('Incorrect choice!!!! ')

main()
