# Daley Ottersbach
# 11/26/2024
# P3HW1
# This program takes a number grade for each of the six modules, determines average and displays letter grade for average along with lowest, 
highest, and sum of grades.

# Enter grades for six modules
def floatput(prompt: str) -> float:
  return float(input(prompt))

mod_1: float = floatput('Enter grade for Module 1: ')
mod_2: float = floatput('Enter grade for Module 2: ')
mod_3: float = floatput('Enter grade for Module 3: ')
mod_4: float = floatput('Enter grade for Module 4: ')
mod_5: float = floatput('Enter grade for Module 5: ')
mod_6: float = floatput('Enter grade for Module 6: ')

# add grades entered to a list
grades: list[float] = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

# determine lowest, highest , sum and average for grades
low: float = min(grades)
high: float = max(grades)
total: float = sum(grades)
avg: float = total / len(grades)

# determine letter grade for average
print()
print("-" * 10 + "Results" + "-" * 10)
print(f"Lowest Grade:  {low:.1f}")
print(f"Highest Grade: {high:.1f}")
print(f"Sum of Grades: {total:.1f}")
print(f"Average:       {avg:.2f}")
print("-" * 27)

if avg >= 90:
  print('Your grade is: A')
elif avg >= 80:
  print('Your grade is: B')
elif avg >= 70:
  print('Your grade is: C')
elif avg >= 60:
  print('Your grade is: D')
else:
  print('Your grade is: F')
