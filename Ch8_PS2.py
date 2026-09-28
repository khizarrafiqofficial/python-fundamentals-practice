def temperature(c):
    return c *(9/5) + 32
    

c = int(input("Enter temperature in celsius: "))
temp = temperature(c)
print(f"{round(temp,2)}°F")