# 015 Ask the user to enter their favourite colour. If they enter “red”, “RED” or “Red” display the message “I like red too”,
# otherwise display the message “I don’t like [colour], I prefer red”.

def color():

    color = input("Enter a color: ")

    if color.lower() == 'red':
        print("I like red too!!!")
    else:
        print("I don't like {0}, I prefer red".format(color))



color()
