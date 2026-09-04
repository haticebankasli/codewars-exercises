def spin_words(sentence):
    word = sentence.split()
    digits=[]
    for n in word:
        if len(n)>=5:
            n = n[::-1]
            digits.append(n)
        else:
            digits.append(n)
    
        
    return" ".join(digits)