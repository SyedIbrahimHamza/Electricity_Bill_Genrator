bills = []


def bill_generator(name, units):
    if units <= 100:
        bill = units * 5
    elif units <= 200:
        bill = 100 * 5 + (units - 100) * 7
    elif units <= 300:
        bill = 100 * 5 + 100 * 7 + (units - 200) * 10
    else:
        bill = 100 * 5 + 100 * 7 + 100 * 10 + (units - 300) * 15

    customer = {
        "name": name,
        "units": units,
        "bill": bill
    }

    bills.append(customer)

    return bill


def total_revenue():
    total = 0

    for customer in bills:
        total += customer["bill"]

    return total


def search_customer(name):
    for customer in bills:
        if customer["name"].lower() == name.lower():
            print("\nCustomer Found!")
            print("Name:", customer["name"])
            print("Units:", customer["units"])
            print("Bill:", customer["bill"])
            return

    print("Customer not found.")


while True:
    print("\n===== ELECTRICITY BILLING SYSTEM =====")
    print("1. Add Customer")
    print("2. Show All Bills")
    print("3. Search Customer")
    print("4. Total Revenue")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter customer name: ")
        units = int(input("Enter units consumed: "))

        bill_generator(name, units)

        print("Customer added successfully!")

    elif choice == "2":
        print("\n===== ELECTRICITY BILLS =====")

        if len(bills) == 0:
            print("No customers found.")
        else:
            for customer in bills:
                print("Name:", customer["name"])
                print("Units:", customer["units"])
                print("Bill:", customer["bill"])
                print("----------------------")

    elif choice == "3":
        name = input("Enter customer name: ")
        search_customer(name)

    elif choice == "4":
        print("Total Revenue:", total_revenue())

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")