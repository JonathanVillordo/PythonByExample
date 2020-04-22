#071 Create a list of two sports. Ask the user what their favourite sport is and add this to the end of the list. Sort the list and display it.

def sports():

    sports = ['basketball','baseball']
    favourite = input('Enter your favourite sport: ')
    sports.append(favourite)
    sports.sort()
    print(sports)

sports()
