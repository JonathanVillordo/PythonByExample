# 044 Ask how many people the user wants to invite to a party.
# If they enter a number below 10, ask for the names and after each name display “[name] has been invited”.
# If they enter a number which is 10 or higher, display the message “Too many people”.

def inviteparty():

    number = int(input("How many persons want to invite to a party: "))

    if number < 10:

        for i in range(1,number+1):
            person = input("Enter a name: ")
            print("{0} has been invited".format(person))

            
inviteparty()
