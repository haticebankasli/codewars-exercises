def duplicate_encode(word):
    word = word.lower()
    new = []
    for n in word:
        if word.count(n) > 1 :
            new.append(")")
        else : 
            new.append("(")
    return "".join(new)