# Write a program to find out whether a given post is talking about “Khizar” or not.
post = input("Enter a post: ")
if("Khizar".lower() in post.lower()):
    print("This post is talking about khizar")
else:
    print("This post is not talking about khizar")
