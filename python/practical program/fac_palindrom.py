def factorial(num):
    if num ==1:
        return 1
    else:
        return num*factorial(num-1)
n = int(input("Enter a number:"))
if n%2==0:
    num = str(n)
    if num == num[::-1]:
        print("The number is palindrome")
    else:
        print("The number is not palindrome")
else:
    print("The factorial of number is",factorial(n))
    factorial_result = factorial(n)
    count = 0
    while factorial_result>0:
        factorial_result=factorial_result // 10
        count +=1
    print("The number of digits in factorial is",count)