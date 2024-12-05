
# Daley Ottersbach
# 11/26/2024
# P3HW2
# Handles employee pay given hours, and payrate before displaying the information

# Get employee name
# Get employee hours
# Get employee pay rate
# If employee hours is more than forty, calculate overtime pay
# Calculate regular pay
# Calculate gross pay, sum of regular and overtime pay
# Display employee name
# Display employee pay rate
# Display employee hours
# Display employee overtime hours
# Display employee regular pay
# Display employee overtime pay
# Display employee gross pay

name: str = input("Employee Name: ")
hours: int = int(input("Employee Hours: "))
pay_rate: float = float(input("Employee Pay Rate: "))

regular_pay: float = min(40, hours) * pay_rate
overtime_hours: int = max(0, hours - 40)
overtime_pay: float = 0
if (overtime_hours > 0):
 overtime_pay = overtime_hours * pay_rate * 1.5

gross_pay: float = regular_pay + overtime_pay

print("-" * 70)
print(f'''{"Employee Name:":<15}{name:<55}\n''')

print(f'''{"Hours":<5} | {"Pay Rate":<8} | {"Overtime":<8} | {"Overtime Pay":<12} | {"Regular Pay":<11} | {"Gross Pay":<12}''')
print(f'''{hours:<5} | ${pay_rate:<7.2f} | {overtime_hours:<8} | ${overtime_pay:<11.2f} | ${regular_pay:<10.2f} | ${gross_pay:<11.2f} ''')
print("-" * 70)
