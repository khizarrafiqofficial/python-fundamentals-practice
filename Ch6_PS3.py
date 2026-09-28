t1 ="Make a lot of money"
t2 ="buy now" 
t3 ="subscribe this" 
t4 ="click this"

comment = input("Enter comment: ")

if((t1 in comment) or (t2 in comment) or (t3 in comment) or (t4 in comment)):
    print("This comment is a spam")
else:
    print("This comment is not a spam")
