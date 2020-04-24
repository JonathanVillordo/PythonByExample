#082 Show the user a line of text from your favourite poem and ask for a starting and ending point. Display the characters between those two points.

def poem():

    poem = 'If you can trust yourself when all men doubt you'
    print(poem)
    start = int(input('Enter a start point: '))
    end = int(input('Enter a end point: '))

    print(poem[start:end])
poem()
