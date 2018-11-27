def say_hi():
    print('Hi, this is my module')
    print('Hi, runned by:', __name__)
    print("Hi, runned by:", __name__)

def mypower(data, n):
    if n < 0:
        return 1.0/pospower(data, -n);
    elif n == 0:
        return 1;
    else:
        return pospower(data, n);

def pospower(data, n):
    if n == 1:
        return data;
    half = pospower(data, n//2);

    if (half%2):
        return data * half * half;
    else:
        return half * half;


__version__ = '0.1'
