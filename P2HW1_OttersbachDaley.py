# Daley Ottersbach
# 11/19/2024
# P2HW1
# Calculates travel expenses taking budget, gas cost, accomodations cost, and food cost into account, before displaying information to user.

def floatput(prompt: str) -> float:
 return float(input(prompt))

print("This program calculates and displays tavel expenses")

budget: float = floatput("Enter Budget: ")
destination: str = input("Enter your travel destination: ")
gasCost: float = floatput("Gas cost: ")
accomodationsCost: float = floatput("Accomodations cost: ")
foodCost: float = floatput("Food cost: ")

print(("-" * 12) + "Travel Expenses" + ("-" * 12))
print(f"Location:               {destination}")
print(f"Initial budget:         ${budget:.2f}")
print(f"Fuel expenses:          ${gasCost:.2f}")
print(f"Accomodations expenses: ${accomodationsCost:.2f}")
print(f"Food expenses:          ${foodCost:.2f}")
print(("-" * 12) + "---------------" + ("-" * 12))
print(f"\nRemaining balance:      ${(budget - (gasCost + accomodationsCost + foodCost)):.2f}")
