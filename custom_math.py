def sum(x, y):
    return x + y

def division(x, y):
    if y == 0:
        raise ValueError("Divider is 0")
    return x / y