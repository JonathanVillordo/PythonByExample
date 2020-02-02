# 006 Ask how many slices of pizza the user started with and
# ask how many slices they have eaten. Work out how many slices they have left and display the answer in a user- friendly format.

def eat():
    a = int(input("Enter How many slices of pizza you started with: "))
    b = int(input("How many slices you have eaten? "))

    print('You have',a-b,'slices of pizza')


eat()
