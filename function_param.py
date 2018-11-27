def print_max(a, b):
    if a > b:
        print(a, 'is the maximum')
    elif a == b:
        print(a, 'is equal to', b)
    else:
        print(b, 'is the maximum')
        print('{0} is the maximum' .format(b))
    return a + b;

c = print_max(3,4)
print('total:', c)
