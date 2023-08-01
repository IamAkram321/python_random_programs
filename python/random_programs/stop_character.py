'''Write a python program to print the input string upto stop character'''
a = input("Enter the string:")
print(a)
stop=input("Enter the stop character:")
for i in a:
       if i==stop: 
              break
       else:
              print(i,end='')
