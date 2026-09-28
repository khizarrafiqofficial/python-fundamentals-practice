from functools import reduce
l = [123, 345, 55, 7898, 985, 34]
def greater (a, b):
    if (a>b):
        return a
    return b

print(reduce(greater, l))