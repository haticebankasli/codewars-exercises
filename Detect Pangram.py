def is_pangram(st):
    new = st.lower()
    withoutduplicate = set(new)
    letters = set()
    for character in withoutduplicate:
        if character.isalpha():
            letters.add(character)
    return len(letters) == 26