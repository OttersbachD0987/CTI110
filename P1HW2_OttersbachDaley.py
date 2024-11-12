# Daley Ottersbach
# 11/12/2024
# P1HW2
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
print(f"Location: {destination}")
print(f"Initial budget: {budget}")
print(f"Fuel expenses: {gasCost}")
print(f"Accomodations expenses: {accomodationsCost}")
print(f"Food expenses: {foodCost}")
print(f"Remaining budget: {budget - (gasCost + accomodationsCost + foodCost)}")