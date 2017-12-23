'''
Name: Hana Chaudhury

This was developed for an assignment for CISC 101 at Queen's University.
Using two lists, this program determines which friends from one list you have not
invited to the party you are throwing. It has been built using pre-populated
lists.

'''

#defines the function

def party():
    
    #welcomes them to the program and outlines what will happen
    print("Welcome! Let's find out who's invited to the party.") 

    #lists are created that while be referenced in the loop later on in the program 
    #creates a list of your Facebook friends
    facebookFriends = ["Tom", "Jim", "Pat", "Ally", "Beatrice", "Heather", "Chelsea", "Mike", "Jade", "Kaila", "Tina", "Caroline"]

    #a list of the friends that have been invited to the party 
    invitedFriends = ["Tina", "Caroline", "Kaila", "Jade", "Heather", "Chelsea"]

    #an empty list to hold all the friends who have not been invited to the party 
    notInvitedFriends = []    

    #a for loop that compares the two lists -- the first line references the  items in list facebookFriends
    for name in facebookFriends:

        #within the for loop this then tells the program to check which elements that are in facebookFriends
        #are NOT in invitedFriends
        #it is comparing the two lists 
        if name not in invitedFriends:

            #adds the resulting names in facebookFriends that are not in invitedFriends to a new list
            notInvitedFriends.append(name)

            #prints the names of all the people not invited in the party 
            print(name, "is not invited to the party")

    #this if statement tells you you haven't invited any friends if your invitedFriends list is empty 
    if len(notInvitedFriends) == 0:
        print("You have no friends invited.")

    #this elif statement tells you you have no Facebook friends if your FB friends list is empty
    elif len(facebookFriends) == 0:
        print("You have no Facebook friends.")


party()



