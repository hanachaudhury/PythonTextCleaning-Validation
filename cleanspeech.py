'''
This program was created for a CISC 101 Assignment at Queen's University.
It takes a speech and removes all punctuation and converts
it to all lower case words. It then prints the list of unique words in the passage
and returns (not the return function) the number of times it appears in the speech.

Name: Hana Chaudhury
'''
def hamlet():

    #string of punctuation that will be needed to remove punctuation
    punctuation = "!,',.,;,?,:,,"

    #speech we will be using for the program 
    hamlet_speech ='''
        To be, or not to be, that is the question:
        Whether 'tis nobler in the mind to suffer
        The slings and arrows of outrageous fortune,
        Or to take Arms against a Sea of troubles,
        And by opposing end them: to die, to sleep
        No more; and by a sleep, to say we end
        the heart-ache, and the thousand natural shocks
        that Flesh is heir to? 'Tis a consummation
        devoutly to be wished. To die, to sleep,
        To sleep, perchance to Dream; aye, there's the rub,
        for in that sleep of death, what dreams may come,
        when we have shuffled off this mortal coil,
        must give us pause. There's the respect
        that makes Calamity of so long life:
        For who would bear the Whips and Scorns of time,
        the Oppressor's wrong, the proud man's Contumely,
        the pangs of despised Love, the Law’s delay,
        the insolence of Office, and the spurns
        that patient merit of the unworthy takes,
        when he himself might his Quietus make
        with a bare Bodkin? Who would Fardels bear,
        to grunt and sweat under a weary life,
        but that the dread of something after death,
        the undiscovered country, from whose bourn
        no traveller returns, puzzles the will,
        and makes us rather bear those ills we have,
        than fly to others that we know not of.
        Thus conscience does make cowards of us all,
        and thus the native hue of Resolution
        Is sicklied o'er, with the pale cast of Thought,
        And enterprises of great pitch and moment, 
        with this regard their Currents turn awry,
        And lose the name of Action. Soft you now,
        The fair Ophelia? Nymph, in thy Orisons
        Be all my sins remembered.'''

    #PART 1: REMOVE PUNCTUATION FROM PASSAGE 
    #create an empty string that will hold the unpunctuated speech 
    unpunctuated_speech = ''

    #creation of a for loop to unpunctuate the speech
    for char in hamlet_speech:    #refers to each individual element
        #if statement that pulls every character not in punctuation list
        if char not in punctuation:
            unpunctuated_speech += char
    #print(unpunctuated_speech)

    #makes everything lower case 
    unpunctuated_speech = unpunctuated_speech.lower()
    
    #PART 2: SPLIT SO EACH WORD IS ELEMENT IN A LIST 
    #split at every white space
    unpunctuated_speech = unpunctuated_speech.split()

    #PART 3: PRINT LIST OF UNIQUE WORDS AND NUMBER OF TIMES THEY APPEAR

    #creates an empty dictionary that will hold all unique words and
    #number of times it appears 
    unique_words = {}

    #looks at every word in the unpunctuated speech 
    for word in unpunctuated_speech:
        if word in unique_words:
            #every time it sees the word appear again it adds to the count
            unique_words[word] += 1
        #if the word only appears once it is assigned a value of one
        #this ensures that if the word is not unique it is added to the count
        #only added to the dictionary if it doesn't see it there
        else:
            unique_words[word] = 1

    #prints the number of unique words and the number of times it appears
    #by printing the dictionary as a string
            
    for word, number in unique_words.items():
        print(word, ":", number)

hamlet() 
    
