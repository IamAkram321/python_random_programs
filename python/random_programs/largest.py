def largest(a,b,c):
    large=a
    if b>large:
      large=b
    if c>large:
      large=c
    return large
num1=float(input("Enter number 1:"))
num2=float(input("Enter number 2:"))
num3=float(input("Enter number 3:"))
result=largest(num1,num2,num3)
print(result,"is the largest")