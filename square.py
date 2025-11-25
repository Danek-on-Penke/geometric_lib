def area(a):
    "Принимает число a, выдает произведение a на a"
    if (type(a) != int and type(a) != float) or (a < 0):
        if type(a) != int and type(a) != float:
            raise TypeError
        else:
            raise ValueError
    else:
        return a * a

def perimeter(a):
    "Принимает число a, выдает произведение a на 4"
    if (type(a) != int and type(a) != float) or (a < 0):
        if type(a) != int and type(a) != float:
            raise TypeError
        else:
            raise ValueError
    else:
        return 4 * a