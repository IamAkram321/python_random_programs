def fac(n):
    if n==1:
        return n
    elif n==0:
        return 1
    else:
        return n*fac(n-1)
i = int(input("Enter a number: "))
f = fac(i)
print(f)