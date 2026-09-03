def pig_it(text):
    words = text.split()
    punctuation = "!?.,"
    new_words = []

    for n in words:
        if n in punctuation:
            new_words.append(n)
        else:
            second = f"{n[1:]}{n[0]}ay"
            new_words.append(second)

    return " ".join(new_words)