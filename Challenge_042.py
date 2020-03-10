# 042 Set a variable called total to 0. Ask the user to enter five numbers and after each input ask them if they want that number included.
# If they do, then add the number to the total. If they do not want it included, don’t add it to the total. After they have entered all five numbers, display the total.
def sumnumbers():
    total = 0

    for i in range(5):
        number = int(input("Enter a number: "))
        inlcude = input("Do you want include? Y or N: ")

        if inlcude.lower() == 'y':
            total += number

    print("Your total is {0}".format(total))

sumnumbers()
