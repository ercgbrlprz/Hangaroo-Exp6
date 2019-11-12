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
    