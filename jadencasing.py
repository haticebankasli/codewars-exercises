def to_jaden_case(string):
    words = string.split()
    words= [word.capitalize() for word in words]
    return " ".join(words)