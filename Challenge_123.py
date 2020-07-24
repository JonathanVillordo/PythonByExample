#123
import csv

def add_file():

    name = input('Enter your name: ')
    salary = input('Enter your salary: ')
    
    file = open('Salary.csv','w')
    new_record = (name + "," + salary)
    file.write(str(new_record))
    file.close()


def view_file():
    
    file = open('Salary.csv','r')
    for row in file:
        print(row)
    file.close()

def delete_file():
    
    file = list(csv.reader(open("Salary.csv")))
    tmp = []

    for row in file:
        tmp.append(row)
    
    x = 0
    for row in tmp:
        display = x,tmp[x]
        print(display)
        x += 1
    get_rid = int(input('Enter a number to delete: '))
    del tmp[get_rid]

    x = 0
    file = open('Salary.csv','w')
    file.write(str(tmp))
    file.close()

def main():

    keep = True

    while keep:
        option = int(input('1) Add to file''\n'
                 '2) View all records''\n'
                 '3) Delete a record''\n'
                 '4) Quit program''\n\n\n'
                 'Enter an option: '
            ))
        if option == 1:
            add_file()
        elif option == 2:
            view_file()
        elif option == 3:
            delete_file()
        elif option == 4:
            keep = False
        else:
            print('Incorrect choice!!!!''\n')
    
main()


