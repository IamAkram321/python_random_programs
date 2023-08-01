a = int(input("Enter a positive integer:"))
if a<0:
    raise Exception("Not a negative number")
else:
    print("Great you entered positive number")