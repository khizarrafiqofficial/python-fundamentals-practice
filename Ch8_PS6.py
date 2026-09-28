def inches_to_cms(inches):
    return inches * 2.54

n = int(input("Enter the value in inches: "))
print(f"The value in cms is: {inches_to_cms(n)}")