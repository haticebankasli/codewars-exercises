def zero(no=None):
    if no is None:
        return 0
    else:
        return no(0)
    
def one(no=None):
    if no is None:
        return 1
    else:
        return no(1)
    
def two(no=None):
    if no is None:
        return 2
    else:
        return no(2)
def three(no=None):
    if no is None:
        return 3
    else:
        return no(3)
def four(no=None):
    if no is None:
        return 4
    else:
        return no(4)
def five(no=None):
    if no is None:
        return 5
    else:
        return no(5)
    
def six(no=None):
    if no is None:
        return 6
    else:
        return no(6)
def seven(no=None):
    if no is None:
        return 7
    else:
        return no(7)
def eight(no=None):
    if no is None:
        return 8
    else:
        return no(8)
    
def nine(no=None):
    if no is None:
        return 9
    else:
        return no(9)

def plus(no1):
    def operation(no2):
        return no1 + no2
    return operation
    
def minus(no1):
    def operation(no2):
        return no2-no1
    return operation

def times(no1):
    def operation(no2):
        return no1 * no2
    return operation
def divided_by(no1):
    def operation(no2):
        return  no2//no1
    return operation