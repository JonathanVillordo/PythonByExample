# 121
def get_menu():
    option = input('Select an option:'' \n'
           'A) Add Name' '\n'
           'B) Change Name''\n'
           'C) Delete Name'' \n'
           'D) Exit''\n')

    if option in ('A','B','C','D'):
        return option
    else:
        print('Incorrect choice!!!')

def add_names(names):
    name = input('Add a name: ')
    names.append(name)
    
    return names

def changes_names(names):
    replace_name = input('Enter a name to be changed: ')
    new_name = input('Enter new name: ')
    names.remove(replace_name)
    names.append(new_name)

    return names

def delete_names(names):
    remove_name = input('Delete a name: ')
    names.remove(remove_name)

def print_names(names):

    for name in names:
        print(name)

def main ():

    names = ['Jonathan']
    option = 'A'

    print_names(names)
    while option in ('A','B','C'):
        option = get_menu()
        if option == 'A':
            add_names(names)
            print_names(names)
        elif option == 'B':
            changes_names(names)
            print_names(names)
        elif option == 'C':
            delete_names(names)
            print_names(names)

main()
