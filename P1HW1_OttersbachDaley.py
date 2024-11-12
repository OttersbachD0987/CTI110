# Daley Ottersbach
# 11/12/2024
# P1HW1
# Uses user input to calculate an exponent and to add and subtract numbers before printing them.

def intput(prompt: str) -> int:
    return int(input(prompt))

def bordered(toBorder: str, border: str, repetition: int) -> str:
    return (border * repetition) + toBorder + (border * repetition)

print(bordered("Calculating Exponents", "-", 5))

baseValue: int = intput("Enter base value: ")
exponenet: int = intput("Enter exponent: ")

print(f"{baseValue} raised to the power of {exponenet} is {baseValue ** exponenet}!!")

print(bordered("Addition and Subtraction", "-", 5))

initialValue: int = intput("Enter starting value: ")
addValue: int = intput("Enter the number to add: ")
subValue: int = intput("Enter the number to subtract: ")

print(f"{initialValue} + {addValue} - {subValue} is equal to {initialValue - subValue + addValue}")
