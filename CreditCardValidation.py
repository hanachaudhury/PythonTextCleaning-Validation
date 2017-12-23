'''
Name: Hana Chaudhury
This was developed for an assignment for CISC 101 at Queen's University.

This question performs a validation check on credit cards. The credit card number will be 8 numbers in length.
The program first determines if you have entered an 8-digit number then validates it.

In order to validate it first takes the result of the sum of every other digit starting from the right.
Then it doubles the numbers not used in step 1, again from the right. It then sums the digits of the resulting
doubled numbers. (i.e. if the doubled value is 56, the digits sum is 5 + 6 = 11). Then it takes the sum of the two
preceding steps and if this result ends in a 0 the card is valid, otherwise it is not. 

The program uses lists multiple for loops in order to accomplish this task to validate the card number. 

'''

def creditCard(): 

    #asks the user to input their credit card number and puts it in a list 
    userInput = input("Please enter your 8-digit credit card number: ")
    creditCard = list(userInput)

    #checks that the user inputted an 8 digit number and if not asks them to re-enter until it is 8 digits 
    while len(creditCard) != 8:
        
        userInput = input("You didn't enter an 8-digit number. Please re-enter a 8-digit credit card number: ")
        
        #allows the loop to jumb back if it's not 8 digits in lengt
        creditCard = list(userInput)

    #set sums to 0 to be referenced in for loops 
    firstSum = 0
    secondSum = 0

    #creates an empty list to hold all the doubled values 
    doubles = []

    #creates a new list to hold all the doubled values split into individual integers i.e. [18] is now [1,8] 
    doubledValuesSplit = []

                                            # --- STEP 1 --- #
    
    #converts every element in the credit card list (which user enters as a string) into integers
    for i in range(len(creditCard)):
        creditCard[i] = int(creditCard[i])
        
    #the for loop references every other element starting from the right and sums those digits                     
    for digit in (creditCard[-1::-2]):
        firstSum += digit

                            # ---  EXPLANATION OF STEP 2 (because it's confusing) --- #
    #this doubles the values and then puts the doubled values in a new list
    #this new list now is converted to a string in order to split each digit up
    #the string is then converted into a list that contains each individual digit so we can get a sum of these values 

                                            
    #this for loop references every other element NOT in the first step 
    for number in creditCard[-2::-2]:
        
        #creates a new variable that doubles each element in creditCard and then adds to a new list
        number = number * 2
        doubles.append(number)
        

    #this looks for i throughout the doubles list you have just created
    for i in range(len(doubles)):
        
        #create a new string and name it and convert every element into a string 
        currentNumber = str(doubles[i])

        #creates a nested loop to take every digit in the string and put them in a new list of integers
        for j in range(0, len(currentNumber)):
            doubledValuesSplit.append(int(currentNumber[j]))
            

    #sums each number in doubledValuesSplit to find the second sum
    for digit in doubledValuesSplit:
        secondSum += digit

                                    # --- EXPLANATION OF STEP 3 --- # 
    #this section of the code performs the validation by adding the two sums and determining
    #if the sum of the numbers produces a valid value
    

    #totals both sums and then remainder determines if last digit is 0 by dividing by 10
    total = firstSum + secondSum
    remainder = total % 10

    #card is VALID if remainder is 0 because if it eneds in 0 it should divide perfectly into 10
    if remainder == 0:
        print("Your credit card is valid!")

    #if the remainder is anything else than 0 the card is invalid 
    else:
        print("Your credit card is invalid!")

creditCard() 
