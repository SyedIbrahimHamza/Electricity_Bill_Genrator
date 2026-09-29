# Electricity Bill Generator

A simple terminal-based Electricity Billing System built with Python.

This program allows users to add customers, calculate electricity bills based on units consumed, view all bills, search for customers, and calculate total revenue.

## Features

* Add customer
* Calculate electricity bill
* Store customer information
* Show all bills
* Search customer by name
* Calculate total revenue
* Menu-based system
* Exit the program
* Handle empty customer list

## Electricity Bill Rates

The electricity bill is calculated according to the number of units consumed.

| Units Consumed  | Rate                            |
| --------------- | ------------------------------- |
| Up to 100 units | Rs. 5 per unit                  |
| 101 - 200 units | Rs. 7 per unit after first 100  |
| 201 - 300 units | Rs. 10 per unit after first 200 |
| Above 300 units | Rs. 15 per unit after first 300 |

### Example

If a customer uses **250 units**:

```text
First 100 units  = 100 × 5  = Rs. 500
Next 100 units   = 100 × 7  = Rs. 700
Next 50 units    = 50 × 10  = Rs. 500

Total Bill = Rs. 1700
```

## Program Menu

The program provides five options:

```text
===== ELECTRICITY BILLING SYSTEM =====
1. Add Customer
2. Show All Bills
3. Search Customer
4. Total Revenue
5. Exit
```

## 1. Add Customer

The user can add a new customer by entering their name and electricity units consumed.

Example:

```text
Enter your choice: 1
Enter customer name: Ali
Enter units consumed: 250
Customer added successfully!
```

The program calculates the electricity bill and stores the customer's information.

Each customer is stored with:

* Name
* Units consumed
* Bill amount

## 2. Show All Bills

This option displays all customers currently stored in the system.

Example:

```text
===== ELECTRICITY BILLS =====
Name: Ali
Units: 250
Bill: 1700
----------------------
```

If there are no customers:

```text
No customers found.
```

## 3. Search Customer

This option allows the user to search for a customer by name.

The search is **case-insensitive**.

For example, searching for:

```text
ali
```

can find:

```text
Ali
```

Example:

```text
Enter customer name: ali

Customer Found!
Name: Ali
Units: 250
Bill: 1700
```

If the customer does not exist:

```text
Customer not found.
```

## 4. Total Revenue

This option calculates the total amount of all electricity bills stored in the system.

Example:

```text
Total Revenue: 3500
```

## 5. Exit

This option exits the program.

Example:

```text
Thank you!
```

## How the Program Works

1. An empty `bills` list is created.
2. The program displays the electricity billing menu.
3. The user selects an option.
4. If option `1` is selected, the user enters the customer name and units consumed.
5. The `bill_generator()` function calculates the electricity bill.
6. Customer information is stored in a dictionary.
7. The dictionary is added to the `bills` list.
8. Option `2` displays all stored customer bills.
9. Option `3` searches for a customer by name.
10. Option `4` calculates total revenue.
11. Option `5` exits the program.
12. The program continues running until the user chooses to exit.

## Functions

### `bill_generator(name, units)`

Calculates the electricity bill according to the number of units consumed.

It also creates a customer dictionary and adds it to the `bills` list.

### `total_revenue()`

Calculates the total revenue by adding the bills of all customers.

### `search_customer(name)`

Searches for a customer by name.

The search uses `.lower()` so that uppercase and lowercase letters do not affect the search.

## Data Storage

The program uses a **list** to store customers.

```python
bills = []
```

Each customer is stored as a **dictionary**:

```python
customer = {
    "name": name,
    "units": units,
    "bill": bill
}
```

The dictionary is then added to the list:

```python
bills.append(customer)
```

## Python Concepts Used

This project practices the following Python concepts:

* Variables
* Functions
* Lists
* Dictionaries
* `if`
* `elif`
* `else`
* `for` loops
* `while` loops
* `break`
* `input()`
* `int()`
* `len()`
* `.lower()`
* `.append()`
* Dictionary keys and values
* Arithmetic operations
* Comparison operators
* Function arguments
* `return`
* User input
* Menu-driven programs

## Project Structure

```text
electricity-billing/
│
├── Electricity_Bill_Genrator.py
└── README.md
```

## How to Run

### 1. Install Python

Make sure Python is installed on your computer.

Check the Python version:

```bash
python --version
```

### 2. Save the Program

Save the Python code as:

```text
Electricity_Bill_Genrator.py
```

### 3. Run the Program

Open a terminal in the project directory and run:

```bash
python Electricity_Bill_Genrator.py
```

## Example Program Flow

```text
===== ELECTRICITY BILLING SYSTEM =====
1. Add Customer
2. Show All Bills
3. Search Customer
4. Total Revenue
5. Exit

Enter your choice: 1
Enter customer name: Ali
Enter units consumed: 150
Customer added successfully!

===== ELECTRICITY BILLING SYSTEM =====
1. Add Customer
2. Show All Bills
3. Search Customer
4. Total Revenue
5. Exit

Enter your choice: 2

===== ELECTRICITY BILLS =====
Name: Ali
Units: 150
Bill: 850
----------------------
```

## Purpose

This project is created for Python practice and learning.

It helps beginners understand how functions, lists, dictionaries, loops, conditions, user input, and arithmetic operations can be combined to create a simple electricity billing system.

## License

This project is intended for educational and practice purposes.
