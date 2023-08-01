x_elements = input("Enter elements for set X:").split()
x = set(x_elements)
y_elements = input("Enter elements for set Y:").split()
y = set(y_elements)
z_elements = input("Enter elements for set Z:").split()
z = set(z_elements)
if x.issubset(y) and x.issubset(z):
    print("Set X is subset of Set Y and Set Z ")
elif x.issubset(y):
    print("Set X is subset of Set Y")
elif x.issubset(z):
    print("Set X is subset of Set Z")
else:
    print("Set X is not subset of other")

if y.issubset(x) and x.issubset(z):
    print("Set Y is subset of Set X and Set Z ")
elif y.issubset(x):
    print("Set Y is subset of Set X")
elif y.issubset(z):
    print("Set Y is subset of Set Z")
else:
    print("Set Y is not subset of other")

if z.issubset(x) and x.issubset(y):
    print("Set Z is subset of Set X and Set Y ")
elif z.issubset(x):
    print("Set Z is subset of Set X")
elif z.issubset(y):
    print("Set Z is subset of Set Y")
else:
    print("Set Z is not subset of other")