def area(a, h):
    "Принимает числа a и h, выдает произведение a на h, деленное на 2"
    if (type(a) != int and type(a) != float) and ((type(h) != int and type(h) != float)) or (a < 0) or (h < 0):
        if type(a) != int and type(a) != float and type(h) != int and type(h) != float:
            raise TypeError
        else:
            raise ValueError
    else:
        return a * h / 2 


def perimeter(a, b, c):
    "Принимает числа a, b, c, выдает сумму этих чисел"
    if (type(a) != int and type(a) != float and type(b) != int and type(b) != float and type(c) != int and type(c) != float) or (a < 0) or (b < 0) or (c < 0):
        if type(a) != int and type(a) != float and type(b) != int and type(b) != float and type(c) != int and type(c) != float:
            raise TypeError
        else:
            raise ValueError
    else:
        if a + b > c and a + c > b and b + c > a:
            return a + b + c
        else:
            raise ValueError