#074 Enter a list of ten colours. Ask the user for a starting number between 0 and 4 and an end number between 5 and 9.
#Display the list for those colours between the start and end numbers the user input.

def colors():

    colors = ['blue','yellow','green','purple','gray','balck','white','gray','red','orange']
    start = int(input('Enter a number between 0 and 4: '))
    end = int(input('Enter a number between 5 and 9: '))

    print(colors[start:end])
colors()
