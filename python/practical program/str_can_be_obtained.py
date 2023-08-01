a = input("Enter first string:")
b = input("Enter second string:")
i = 0
j = 0
while i<len(a) and j<len(b):
    if a[i]==b[j]:
        j+=1
    i+=1
if j == len(b):
    print("Yes, second string can be obtained")
else:
    print("NO,second string can't be obtained")