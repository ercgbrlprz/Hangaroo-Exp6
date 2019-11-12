def getGuessedWord(secretWord, lettersGuessed):
    
    word = ''
    
    for letter in secretWord:
        
        if letter in lettersGuessed:
            word = word + letter 
            
        else:
            word = word + '_ '
            
    return word


def isGuessedWord(secretWord, lettersGuessed):
    
    correctCtr = 0
    
    for letter in secretWord:
        
        if letter in lettersGuessed:
            correctCtr +=1
        
        else:
            return False
    
    return True


def getAvailableLetters(lettersGuessed):
    
    string = ""
    ctr = 0
    letters = 'abcdefghijklmnopqrstuvwxyz'
    
    for letterguess in letters:
        
        if letterguess in lettersGuessed:
            ctr+=1
        
        else:
            string+=letterguess
    
    return string
    

def hangaroo(secretWord):
    
    secretWord = ('apple')
    
    lettersGuessed = []
    guess = str
    mistakesMade = 5
    wordGuessed = False
    
    print('Welcome to HANGAROO!')
    print('I am thinking of a word with ' + str(len(secretWord)) + ' letters.' )
    print('\n')

    while mistakesMade > 0 and mistakesMade <= 8 and wordGuessed is False:
        
        if secretWord == getGuessedWord(secretWord, lettersGuessed):
            wordGuessed = True
            break
        
        print ('You have ' + str(mistakesMade) + ' chances left.')
        print('Available Letters: ' + getAvailableLetters(lettersGuessed))
        guess = input('Input your guess: ').lower()
        
        if guess in secretWord:
            if guess in lettersGuessed:
                print("And I oop! The letter is already used. Try again. " + getGuessedWord(secretWord, lettersGuessed))
                print ('\n')
            
            else:
                lettersGuessed.append(guess)
                print("Sana all! Good guess! Here is the word now: " + getGuessedWord(secretWord, lettersGuessed))
                print ('\n')
        
        else:
            if guess in lettersGuessed:
                print("Oops! You've already guessed that letter. Here is the word now: " + getGuessedWord(secretWord, lettersGuessed))
                print ('\n')
                
            else:
                lettersGuessed.append(guess)
                mistakesMade -= 1
                print("Oof again! That letter is not in the word. Here is the word now: " + getGuessedWord(secretWord, lettersGuessed))
                print ('\n')

    if wordGuessed == True:
        return print ('You have guessed the word. Congratulations!')
    
    elif mistakesMade == 0:
        print ('Hope you will do better next time! The word was ' + secretWord)

hangaroo(secretWord)