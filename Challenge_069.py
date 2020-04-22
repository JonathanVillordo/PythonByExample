#069 Create a tuple containing the names of five countries and display the whole tuple.
#Ask the user to enter one of the countries that have been shown to them and then display the index number (i.e. position in the list)
#of that item in the tuple

def countries():

    countries = ('USA','Mexico','China','Argentina','Colombia')
    print(countries)
    choose = input('Type a Country :')
    print('Index loaction {}'.format(countries.index(choose)))

countries()

