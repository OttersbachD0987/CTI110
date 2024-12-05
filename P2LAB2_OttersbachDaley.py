# Daley Ottersbach
# 11/19/2024
# P2LAB2
# Calculate gallons of gas needed to travel an amount of miles provided by the user for one of the provided vehicles and display the information.

def floatput(prompt: str) -> float:
 return float(input(prompt))

vehicles: dict[str, float] = {
 "Camaro": 18.21,
 "Prius": 52.36,
 "Model S": 110,
 "Silverado": 26
}

keys = vehicles.keys()

print(f"{keys}")

vehicle: str = input("Enter a vehicle to see it's mpg: ")

print(f"The {vehicle} gets {vehicles[vehicle]:.2f} mpg.")

miles: float = floatput(f"How many miles will you drive the {vehicle}: ")

print(f"{(miles / vehicles[vehicle]):.2f} gallon(s) of gas are needed to drive the {vehicle} {miles:.1f} miles.")
