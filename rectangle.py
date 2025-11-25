def area(a, b):
    "Принимает числа a и b, выдает произведение данных чисел"
    if (type(a) != int and type(a) != float) and ((type(b) != int and type(b) != float)) or (a < 0) or (b < 0):
        if type(a) != int and type(a) != float and type(b) != int and type(b) != float:
            raise TypeError
        else:
            raise ValueError
    else:
        return a * b 


def perimeter(a, b):
    "Принимает числа a и b, выдает произведение суммы данных чисел на 2"
    if (type(a) != int and type(a) != float) and ((type(b) != int and type(b) != float)) or (a < 0) or (b < 0):
        if type(a) != int and type(a) != float and type(b) != int and type(b) != float:
            raise TypeError
        else:
            raise ValueError
    else:
        return 2*(a + b)