m1=int(input("Enter physics marks:"))
m2=int(input("Enter Chemistry marks:"))
m3=int(input("Enter Maths marks:"))
avg=(m1+m2+m3)/3
if avg>=85:
    print("Your grade is:",'O')
if avg>=70:
    print("Your grade is:",'A')
if avg>=60:
    print("Your grade is:",'B')
if avg>=50:
    print("Your grade is:",'C')
else:
    print("Your grade is:",'RA')