def palindrome(num):
    return str(num)==str(num)[::-1]
a=int(input("Enter the number:"))
if palindrome(a):
    print("The number is palindrome")
else:
    print("The number is not palindrome")