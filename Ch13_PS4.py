def divisible5 (n):
    if (n%5 == 0):
        return True
    return False

a = [123, 345, 55, 7898, 985, 34]
f = list(filter(divisible5, a))
print(f)