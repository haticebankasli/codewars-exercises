def high_and_low(numbers):
    number = numbers.split()
    new_numbers = []
    for n in number:
        new_numbers.append(int(n))
    return f"{max(new_numbers)} {min(new_numbers)}"