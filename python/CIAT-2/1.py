print("Handling execption using try...except...else")
try:
    numrator=int(input("Enter numerator:"))
    denom=int(input("Enter denominator:"))
    quotient = (numrator/denom)
    print("Division performed successfully")
except ZeroDivisionError:
    print("You can't enter zero")
except ValueError:
    print("Only integer")
else:
    print("The quotient is",quotient)


    