try:
 a =  int(input("Enter an integer:"))
except ValueError:
 print("Only integer")
else:
 print("It is an integer")