#078 Create a list containing the titles of four TV programmes and display them on separate lines.
#Ask the user to enter another show and a position they want it inserted into the list. Display the list again,
#showing all five TV programmes in their new positions.

def tvshow():

    tvshows = ['fleabag','whatchmen','leaving neverland','russia doll']

    for i in tvshows:
        print(i)

    addshow = input('Add new tv show: ')
    position = int(input('Select  position: '))

    tvshows[position]= addshow

    print(tvshows)
tvshow()

