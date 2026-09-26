bills=[]
def bill_generator(name,units):
    if units<=100:
        bill=units*5
    elif units<=200:
        bill=100*5+(units-100)*7
    elif units<=300:
        bill=100*5+100*7+(units-200)*10
    else:
        bill=100*5+100*7+100*10+(units-300)*15
    bills.append((name,bill))
    return bill
for i in range(3):
    name = input("Enter customer name: ")
    units = int(input("Enter units: "))

    bill_generator(name, units)
print(" ELECTRICITY BILLS ")

for customer in bills:
    print("Name:", customer["name"])
    print("Units:", customer["units"])
    print("Bill:", customer["bill"])
    print("----------------------")