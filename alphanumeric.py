def alphanumeric(password: str) -> bool:
    if password == "":
        return False

    for n in password:
        if not n.isalnum():
            return False

    return True