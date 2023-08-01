a = list(map(int,input("Enter element of list:").split()))
print(a)
sorted_list = sorted(a)
if a == sorted_list:
    print("The list is in ascending order")
else:
    print("The list is not in ascending order")