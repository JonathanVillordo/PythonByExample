#048 Ask for the name of somebody the user wants to invite to a party. After this, display the message “[name] has now been invited”
#and add 1 to the count. Then ask if they want to invite somebody else. Keep repeating this until they no longer want to invite anyone
#else to the party and then display how many people they have coming to the party.

def party():
  
  invited = 0
  onemore = 'y'

  name = input("Enter a name for the party: ")
  print ("{0} has now been invited".format(name))
  invited = 1

  while onemore == 'y':
    onemore = input("Do you want invite one more? ")
    invited = invited + 1
  print("Number of invited persons {0}".format(invited))
  
party()
