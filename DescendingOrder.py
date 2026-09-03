def descending_order(num):
    digits = str(num)
    digits = sorted(digits,reverse=True)
    result = "".join(digits)
    return int(result)