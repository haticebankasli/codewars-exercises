def create_phone_number(n):
    first = "".join(str(number)for number in n[0:3])
    second = "".join(str(number) for number in n[3:6])
    third = "".join(str(number) for number in n[6:])
    return f"({first}) {second}-{third}"