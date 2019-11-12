def isWordGuessed (secretWord, lettersGuessed):
    
    for letters in secretWord:
       
        if letters not in lettersGuessed:
            return False
            
        else:
            return True