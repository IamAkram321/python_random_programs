def palindrome(num):
    return str(num)==str(num)[::-1]
def fac(n):
    if n==1:
        return n
    elif n==0:
        return 1
    else:
        return n*fac(n-1)
number=int(input("Enter your number:"))
if number%2==0:
    result=fac(number)
    print("The factorial of num",number, 'is:',result)
else:
    if palindrome(number):
        print("The number",number,'is palindrome')
    else:
        print("The number",number,'is not palindrome')

