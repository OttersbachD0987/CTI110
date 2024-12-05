# Daley Ottersbach
# 11/26/2024
# P2HW2
# Intakes grades for modules 1 through 6, outputs the lowest, highest, sum of, and average of the grades

# Enter grades    (module 1-6)
# Store in list
# Display Lowest  (min)
# Display Highest (max)
# Display Sum     (sum)
# Display Average (sum / len)
grades: list[float] = []

# Go through modules and get grades
grades.append(float(input(f"Enter grade for Module 1: ")))
grades.append(float(input(f"Enter grade for Module 2: ")))
grades.append(float(input(f"Enter grade for Module 3: ")))
grades.append(float(input(f"Enter grade for Module 4: ")))
grades.append(float(input(f"Enter grade for Module 5: ")))
grades.append(float(input(f"Enter grade for Module 6: ")))

# This is just display stuff
print("-----------------Results-----------------")
print(f"Lowest Grade:       {min(grades):.1f}")
print(f"Highest Grade:      {max(grades):.1f}")
print(f"Sum of Grades:      {sum(grades):.1f}")
print(f"Average:            {(sum(grades)/len(grades)):.2f}")
print("-----------------------------------------")
