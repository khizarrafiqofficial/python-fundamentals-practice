# Write a program which finds out whether a given name is present in a list or not.
l = ["Ahmad", "Ali", "Bilal", "Maham"]

name =input("Enter a name: ")
if(name in l):
    print(name,"is present in list.")
else:
    print(name,"is not present in list.")
