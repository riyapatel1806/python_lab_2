def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a * b
def divide(a,b):
    if b!=0:
        return a/b
    else:
        return"division by zero is not allowed"
def percentage(total,part):
    if total!=0:
        return(part/total)*100
    else:
        return"total can't be zero"