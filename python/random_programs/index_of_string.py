a = input("Enter your string:")
b = input("Enter your search character:")
for i in range(len(a)):
    if b==a[i]:
        print("Your character lies in index",i)
        break
else:
        print("Error")
# if b != a:
#     print("Error")