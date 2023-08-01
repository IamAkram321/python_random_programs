n = int(input("Enter the no. of elements:"))
my_dict={}
for i in range(n):
    key=input("Enter the key:")
    value=input("Enter the value:")
    my_dict[key]=value
print("Dictionary Items are:")
for key, value in my_dict.items():
    print(key,value)