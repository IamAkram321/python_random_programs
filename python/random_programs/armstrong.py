
num = input("Enter a number: ")
num_digits = len(num)
sum = sum(int(digit) ** num_digits for digit in num)

if int(num) == sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
