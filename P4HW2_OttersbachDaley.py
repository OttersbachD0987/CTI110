# Daley Ottersbach
# 12/5/2024
# P4HW2
# The program however will calculate gross pay for multiple employees, determined by user, and also calculates total amount paid for overtime, total amount paid for regular pay and total amount paid for all employees.

# Loop
#   Get employee name
#   If emploee name is Done, break the loop
#   Increment employees
#   Get employee hours
#   Get employee pay rate
#   If employee hours is more than forty, calculate overtime pay
#   Calculate regular pay
#   Calculate gross pay, sum of regular and overtime pay
#   Add overtime pay to total overtime pay
#   Add regular pay to total regular pay
#   Add gross pay to total gross pay
#   Display employee name
#   Display employee pay rate
#   Display employee hours
#   Display employee overtime hours
#   Display employee regular pay
#   Display employee overtime pay
#   Display employee gross pay
# Display total number of employees
# Display total paid for overtime
# Display total paid for regular hours
# Display total paid in gross

employees: int = 0
overtime_total: float = 0
regular_total: float = 0
gross_total: float = 0

while True:
    name: str = input("Employee Name or \"Done\" to terminate: ")
    if (name == "Done"): 
        break
    employees += 1
    hours: int = int(input("Employee Hours: "))
    pay_rate: float = float(input("Employee Pay Rate: "))

    regular_pay: float = min(40, hours) * pay_rate
    overtime_hours: int = max(0, hours - 40)
    overtime_pay: float = 0
    if (overtime_hours > 0):
        overtime_pay = overtime_hours * pay_rate * 1.5

    gross_pay: float = regular_pay + overtime_pay

    overtime_total += overtime_pay
    regular_total += regular_pay
    gross_total += gross_pay

    print("-" * 70)
    print(f'''{"Employee Name:":<15}{name:<55}\n''')

    print(f'''{"Hours":<5} | {"Pay Rate":<8} | {"Overtime":<8} | {"Overtime Pay":<12} | {"Regular Pay":<11} | {"Gross Pay":<12}''')
    print(f'''{hours:<5} | ${pay_rate:<7.2f} | {overtime_hours:<8} | ${overtime_pay:<11.2f} | ${regular_pay:<10.2f} | ${gross_pay:<11.2f} ''')
    print("-" * 70 + "\n\n\n")

print()
print(f"Total number of employees entered: {employees}")
print(f"Total amount paid for overtime: ${overtime_pay:.2f}")
print(f"Total amount paid for regular hours: ${regular_pay:.2f}")
print(f"Total amount paid in gross: ${gross_total:.2f}")