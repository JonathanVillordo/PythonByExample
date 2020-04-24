# 084 Ask the user to type in their postcode. Display the first two letters in uppercase.

def zipcode():

    code = input('Enter zip code: ')
    print(code[0:2].upper())
zipcode()
