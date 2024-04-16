employee_list = []
item_list = []

def print_menu():
    print("-------------------------------")
    print("|   1- Create Employee        |")
    print("|   2- Create Item            |")
    print("|   3- Make Purchase          |")
    print("|   4- All Employee Summary   |")
    print("|   5- Exit                   |")
    print("-------------------------------")


def get_employee_info():
    employees = []

    while True:
        employee_id = input("Enter employee ID (or 'NO' to finish): ")
        if employee_id.upper() == "NO":
            break

        if any(existing_emp[0] == employee_id for existing_emp in employees):
            print("Employee ID must be unique. Please enter a different ID.")
            continue

        employee_name = input("Enter employee name: ")
        employee_type = input("Enter employee type (hourly/manager): ")
        if employee_type.lower() not in ["hourly", "manager"]:
            print("Invalid employee type. Please enter 'hourly' or 'manager'.")
            continue

        years_worked = input("Enter years worked: ")
        if not years_worked.isdigit():
            print("Years worked must be a number.")
            continue

        total_purchased = 0
        total_discounts = 0
        employee_discount_number = input("Enter employee discount number: ")
        if not employee_discount_number.isdigit():
            print("Employee discount number must be a number.")
            continue

        employees.append(
            [employee_id, employee_name, employee_type, int(years_worked), total_purchased, total_discounts,
             int(employee_discount_number)])

    return employees


def get_item_info():
    items = []

    while True:
        item_number = input("Enter item number (or 'NO' to finish): ")
        if item_number.upper() == "NO":
            break

        if any(existing_item[0] == item_number for existing_item in items):
            print("Item number must be unique. Please enter a different number.")
            continue

        item_name = input("Enter item name: ")
        if not item_name:
            print("Item name cannot be empty.")
            continue

        item_cost = input("Enter item cost: ")
        if not item_cost.isdigit():
            print("Item cost must be a number.")
            continue

        items.append([item_number, item_name, int(item_cost)])

    return items


def get_employee_by_discount_number(employees_list, discount_number):
    for employees in employees_list:
        if str(employees[6]) == discount_number:
            return employees
    return None

def make_purchase(employee_list, item_list):
    while True:
        print("Available Items:")
        print("Item Number | Item Name         | Item Cost")
        for item in item_list:
            print(f"{item[0]}{' ' * (12 - len(str(item[0])))}| {item[1]}{' ' * (17 - len(item[1]))}| ${item[2]:.2f}")

        item_number = input("Enter item number to purchase (or 'NO' to exit): ").lower()
        if item_number == "no":
            break

        valid_items = [item for item in item_list if str(item[0]) == item_number]
        if not valid_items:
            print("Invalid item number. Please enter a valid item number.")
            continue

        employee_discount_number = input("Enter employee discount number: ")

        valid_employee = get_employee_by_discount_number(employee_list, employee_discount_number)
        if not valid_employee:
            print("Invalid employee discount number. Please enter a valid number.")
            continue

        years_worked = int(valid_employee[3])
        employee_type = valid_employee[2]
        total_discounts = valid_employee[5]

        max_discount = min(10, years_worked * 2)
        if employee_type == "manager":
            max_discount += 10

        if total_discounts >= 200:
            discount = 0
        else:
            discount = min(max_discount, 200 - total_discounts)

        for item in valid_items:
            print("\nPurchase Details:")
            print(f"Item Name: {item[1]}")
            print(f"Item Cost: ${item[2]:.2f}")
            print(f"Employee Discount: ${discount:.2f}")
            total_cost = item[2] - discount
            print(f"Total Cost: ${total_cost:.2f}")

        valid_employee[5] += discount

        another_purchase = input("\nAnother purchase? (Yes/No): ").lower()
        if another_purchase == "no":
            break


def print_employee_summary(employee_list):
    header = ("Employee ID | Employee Name | Employee Type "
              "| Years Worked | Total Purchased | Total Discounts | Employee Discount Number")
    print("\nAll Employee Summary Page:")
    print(header)
    for emp in employee_list:
        employee_id = emp[0]
        employee_name = emp[1]
        employee_type = emp[2]
        years_worked = emp[3]
        total_purchased = emp[4]
        total_discounts = emp[5]
        employee_discount_number = emp[6]

        print(
            f"{employee_id}{' ' * (12 - len(str(employee_id)))} | {employee_name}"
            f"{' ' * (16 - len(employee_name))} | {employee_type}{' ' * (14 - len(employee_type))}"
            f" | {years_worked}{' ' * (13 - len(str(years_worked)))} | {total_purchased}"
            f"{' ' * (16 - len(str(total_purchased)))} | {total_discounts}"
            f"{' ' * (16 - len(str(total_discounts)))} | {employee_discount_number}")


print("Welcome to the Menu!")
while True:
    print_menu()
    option = input("Choose an option: ")

    if option == "1":
        print("\nCreating Employee...")
        employee_list = get_employee_info()
        print("\nEmployee information entered:")
        for employee in employee_list:
            print(employee)
    elif option == "2":
        print("\nCreating Item...")
        item_list = get_item_info()
        print("\nItem information entered:")
        for item in item_list:
            print(item)
    elif option == "3":
        print("\nMaking Purchase...")
        make_purchase(employee_list, item_list)
    elif option == "4":
        print("\nAll Employee Summary...")
        print_employee_summary(employee_list)
    elif option == "5":
        print("Exiting the program...")
        break
    else:
        print("Invalid option. Please choose a valid option.")
