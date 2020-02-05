# 008 Ask for the total price of the bill, then ask how many diners there are. Divide the total bill by the number of diners and
# show how much each person must pay.
def totalbill():
    totalbill = int(input("What is the total bill?: "))
    diners = int(input ("How many diners are?: "))

    return totalbill/diners

print(totalbill())
