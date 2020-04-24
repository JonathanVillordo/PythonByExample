#079 Create an empty list called “nums”. Ask the user to enter numbers. After each number is entered, add it to the end of the nums list and display the list.
#Once they have entered three numbers, ask them if they still want the last number they entered saved. 
#If they say “no”, remove the last item from the list. Display the list of numbers.

def numbers():

    nums = []
    for i in range(3):
        number =int (input('Enter a number: '))
        nums.append(number)
    
    remove = input('Do you want keep the las number?: ')

    if remove == 'no':
        nums.pop()

    print(nums)
        

    

numbers()
