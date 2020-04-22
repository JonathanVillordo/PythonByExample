#073 Ask the user to enter four of their favourite foods and store them in a dictionary so that they are indexed with numbers starting from 1.
#Display the dictionary in full, showing the index number and the item. Ask them which they want to get rid of and remove it from the list.
#Sort the remaining data and display the dictionary.

def fruits():

    fruits = {}

    print('Enter 4 favourites fruits')
    for i in range(1,5):
        fruit = input('Enter fruit :')
        fruits[i] = fruit
    
    print(fruits)
    getrid  = int(input('Select a fruit to be removed :'))
    del fruits[getrid]
    print(sorted(fruits.values()))
    

fruits()
