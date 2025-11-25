import math

def area(r):
    "Принимает число r, выводит произведение r на r на π"
    if (type(r) != int and type(r) != float) or (r < 0):
        if type(r) != int and type(r) != float:
            raise TypeError
        else:
            raise ValueError
    else:
        return math.pi * r * r

def perimeter(r):
    "Принимает число r, выдает произведение r на 2 на π"
    if (type(r) != int and type(r) != float) or (r < 0):
        if type(r) != int and type(r) != float:
            raise TypeError
        else:
            raise ValueError
    else:
        return 2 * math.pi * r