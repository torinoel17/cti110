# This is a comment
# Tori Strickland
# 07/01/2024
# Creating program that calulates employee's pay by the hour

def main():
    # Input employee details
    employee_name = input("Enter the employee's name: ")
    hours_worked = float(input("Enter the number of hours worked this week: "))
    pay_rate = float(input("Enter the employee's pay rate: "))

    if hours_worked <= 40:
        regular_pay = hours_worked * pay_rate
        overtime_hours = 0
        overtime_pay = 0
    else:
        # Calculate overtime pay (hours worked beyond 40)
        overtime_hours = hours_worked - 40
        overtime_pay = overtime_hours * (pay_rate * 1.5)
        regular_pay = 40 * pay_rate
    print('-------------------------')

    gross_pay = regular_pay + overtime_pay
    print("\nEmployee Name:",     employee_name)
    print(f"Pay Rate: ${pay_rate:.2f}")
    print(f"Hours Worked: {hours_worked:.2f}")
    print(f"Overtime Hours: {overtime_hours:.2f}")
    print(f"Overtime Pay: ${overtime_pay:.2f}")
    print(f"Regular Pay: ${regular_pay:.2f}")
    print(f"Gross Pay: ${gross_pay:.2f}")


if __name__ == "__main__":
    main()
        
