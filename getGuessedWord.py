def getGuessedWord (secretWord, lettersGuessed):
    
    temp = [_]
    string = ""
    
    for key in secretWord:
        
        if key in lettersGuessed:
            string+=key
            
        else:
            string+="_"
            
    return string