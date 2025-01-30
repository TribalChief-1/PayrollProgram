def employee_name():
    return input("Enter employee name: ")


def get_total_hours():
    while True:
        try:
            hours = float(input("Enter total hours for employee: "))
            if hours < 0:
                print("Hours cannot be negative. Please try again..")
                continue
            return hours
        except ValueError:
            print("Please enter a valid number.. ")


def get_hourly_rate():
    while True:
        try:
            rate = float(input("Enter hourly rate for employee: "))
            if rate < 0:
                print("hourly rate cannot be negative. Please try again..")
                continue
            return rate
        except ValueError:
            print("Please enter a valid number.. ")


def get_tax_rate():
    while True:
        try:
            tax_rate = float(input("Enter income tax rate (as a percentage, e.g., 20 for 20%): "))
            if tax_rate < 0 or tax_rate > 100:
                print("Tax rate must be between 0 and 100. Try again..")
                continue
            return tax_rate / 100
        except ValueError:
            print("Please enter a valid number.. ")


def pay_calculation(hours, rate, tax_rate):
    gross_pay = hours * rate
    income_tax = gross_pay * tax_rate
    net_pay = gross_pay - income_tax
    return gross_pay, income_tax, net_pay


def employee_details(name, hours, rate, gross, tax_rate, tax, net):
    print("\n******** Employee Details ********")
    print(f"Name: {name}")
    print(f"Total hours worked: {hours:.2f}")
    print(f"Hourly Rate: ${rate:.2f}")
    print(f"Gross Pay: ${gross:.2f}")
    print(f"Income Tax Rate: {tax_rate * 100:.2f}%")
    print(f"Income Tax: ${tax:.2f}")
    print(f"Net Pay: ${net:.2f}")
    print("====================================\n")


def totals_display(total_employees, total_hours, total_gross, total_tax, total_net):
    print("\n ******** Company Totals ****** ")
    print(f"Total number of employees: {total_employees}")
    print(f"Total hours worked: {total_hours:.2f}")
    print(f"Total Gross Pay: ${total_gross:.2f}")
    print(f"Total income tax: ${total_tax:.2f}")
    print(f"Total net pay: ${total_net:.2f}")


def main():
    total_employees = 0
    total_hours = 0
    total_gross = 0
    total_tax = 0
    total_net = 0

    while True:
        print("----- Welcome to the Payroll program! -----")
        print("\n Please press enter to continue or type 'end' to stop the program..")
        action = input().strip()
        if action.lower() == "end":
            break

        name = employee_name()
        hours = get_total_hours()
        rate = get_hourly_rate()
        tax_rate = get_tax_rate()

        gross, tax, net = pay_calculation(hours, rate, tax_rate)

        employee_details(name, hours, rate, gross, tax_rate, tax, net)

        total_employees += 1
        total_hours += hours
        total_gross += gross
        total_tax += tax
        total_net += net

        totals_display(total_employees, total_hours, total_gross, total_tax, total_net)






if __name__ == "__main__":
    main()
