a = list(map(int,input("Enter the elements of list:").split()))
print("Original list",a)
b = int(input("Enter the element to search its index:"))
for i in range(len(a)):
    if a[i]==b:
        print("The positive index of list is",i)
        print("The negative index of list is",i-len(a))
        break
else:
    print("Element cannot be found")