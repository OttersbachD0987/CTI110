# Daley Ottersbach
# 11/19/2024
# P2LAB1
# Calculate information about a circle from the radius
from math import pi

def floatput(prompt: str) -> float:
 return float(input(prompt))

radius: float = floatput("Enter the radius of the circle: ")

print(f"The diameter of the circle is {(2 * radius):.1f}")
print(f"The circumference of the circle is {(2 * pi * radius):.2f}")
print(f"The area of the circle is {(pi * radius ** 2):.3f}")
