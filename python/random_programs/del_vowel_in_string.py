a = input("Enter the string")
print(a)
vowel=['a','e','i','o','u']
for i in a:
    if i in vowel:
        continue
    else:
        print(i,end='')
