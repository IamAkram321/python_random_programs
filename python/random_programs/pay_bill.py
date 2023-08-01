def line():
    print('================================')
for i in range(3):
    empid=input("Enter the empid:")
    name=input("Enter the name:")
    bp=int(input("Enter the Basic Pay:"))
    da=bp*20/100
    hra=bp*10/100
    it=bp*8/100
    gp=bp+da+hra
    np=gp-it
    line()
    print('Paybill')
    line()
    print("ID                   :",empid)
    print("Name                 :",name)
    print("Basic Pay            :",bp)
    print("dA                   :",da)
    print("IT                   :",it)
    print("Gross Pay            :",gp)
    print("Net Pay              :",np)
    line()
    break

    