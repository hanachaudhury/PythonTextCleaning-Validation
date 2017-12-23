'''
This was developed for an assignment for CISC 101 at Queen's University.
It pulls a list of 10,000 words from a website, cleans the list
of nonsense words (defined as those words that are repeating characters: i.e. 'aa',
'bbbb', or 'ccc' - does not take into account words like 'abca'). After cleaning the
list the user is prompted as to what option they would like to take: check if
a word is in a list, check the number of words with a certain length, check
the number of words in the list that start with a specific letter. This is all called
in a main function by passing parameters and returning values. The main function
allows the user to quit by entering a specific number.  The individual functions
do not account for the user entering an invalid value. 


Name: Hana Chaudhury 
'''

import urllib.request #this loads a library you will need - put this at top of file.

#returns data from the weppage - this code was provided 
def readWordList():
    response = urllib.request.urlopen("http://www.mit.edu/~ecprice/wordlist.10000")
    html = response.read()
    data = html.decode('utf-8').split("\n")
    return data         #allows us to use it later on 

#this cleans the list by removing words made up of duplicates
#anyList can be assigned whatever we want in our main function to pass through previous data
def cleanList(anyList):
    
    #empty list to hold values 
    clean_list = []

    #for loop that looks through the entire list
    for i in range(len(anyList)-1):
        #assigns variable word to each element in the list 
        word = anyList[i]
        #if statement asks if each element is equal to its length times its first letter
        if word != len(word)*word[0]:
            #adds all the words that aren't repeated characters to a new clean list
            clean_list.append(word)
            
    #returns the clean list so we can call it in later functions 
    return clean_list

#function that allows us to check which word is in the list - anyList is a parameter passed
def wordCheck(anyList):
    #asks for user input for word to check 
    wordInput = input("Please enter what word you would like to check: ")

    #if statement to check if the word is in the list or not 
    if wordInput in anyList:
        print("Word is in list") 
    else:
        print("Word is not in list.")
        
#function that checks the length of the word and number of words with that length
#same parameter passing 
def lengthCheck(anyList):

    #empty list that will hold all the words with N length user enters
    lengthList = []

    #user input for length 
    user_input = int(input("Length of word: "))

    #for loop that checks the passed list 
    for word in anyList:
        #this checks if the length of the every word in the list is equal to input or not
        if len(word) == user_input:
            #if it's equal it adds it to the list 
            lengthList.append(word)

    #assigns variable so we can return the value 
    numberLengths = len(lengthList)
    return numberLengths

#checks all words with word starting with N letter (user input) 
def letterCheck(anyList):

    #empty list that holds all words with the letter starting with N 
    number_of_words = []
    #user enters what the word starts with
    check_letter = input("Please enter what the word starts with: ")

    #for loop checks the whole list 
    for i in range(len(anyList)-1):
        #word variable assigned to every element of the list
        #this is needed so we don't get an index error!
        word = anyList[i]

        #if the first letter of each word in the list is equal to user input
        if word[0] == check_letter:
            #add it to the new list!
            number_of_words.append(word)
            
    #assigns variable with the length of the list that tells us the number
    #of words starting with the letter user inputted and returns value
    result = len(number_of_words)
    return result

#asks user what they'd like to do and quits if they don't want to do anything
def userChoice(clean_list):

    #user input 
    user_choice = int(input("""Option 1: Checks if word is in list.
Option 2: Checks the number of words of length you enter.
Option 3: Checks the number of words with letter N. Enter 0 to quit.
Otherwise enter the number corresponding to which option you want."""))

    #series of if statements that call each corresponding function depending on
    #user choice
    if user_choice == 1:
        wordCheck(clean_list)
        #returns the main function in order to pop the user back up to user choice
        #without an empty value
        #this is needed for parameter passing of the cleaned list data 
        return main() 
    
    if user_choice == 2:
        numberLengths = lengthCheck(clean_list)
        print(numberLengths)
        return main() 
    
    if user_choice == 3:
        letterCheck_number = letterCheck(clean_list)
        print(letterCheck_number)
        return main()

    #quits program 
    if user_choice == 0:
        print("Thanks for using this program!")

    #if user enters an invalid character it prompts them to enter a valid charcater
    else:
        print("Enter valid number.")
        return main() 

#main function that calls the other functions 
def main():
    word_list = readWordList() #word_list is assigned to the returned list
    clean_list = cleanList(word_list)   #clean list needs to refer to the returned data

    #calls the user choice function that calls the rest of the functions
    userChoice(clean_list) 

main()                      
    
 
