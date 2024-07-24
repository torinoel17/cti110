# Tori Strickland
# 06/23/2024
# P2HW2
# Creating a List

# Initialize an empty list to store grades
grades_list = []

# Prompt the user for grades
module_1_grade = float(input("Enter grade for Module 1: "))
module_2_grade = float(input("Enter grade for Module 2: "))
module_3_grade = float(input("Enter grade for Module 3: "))
module_4_grade = float(input("Enter grade for Module 4: "))
module_5_grade = float(input("Enter grade for Module 5: "))
module_6_grade = float(input("Enter grade for Module 6: "))

# Add grades to the list
grades_list.extend([module_1_grade, module_2_grade, module_3_grade, module_4_grade, module_5_grade, module_6_grade])

# Calculate the lowest and highest grades
lowest_grade = min(grades_list)
highest_grade = max(grades_list)

# Calculate the sum of grades
total_grades = sum(grades_list)

# Calculate the average (rounded to 2 decimal places)
average_grade = total_grades / len(grades_list)
print()
print("--------Results--------")
# Display the results
print(f"Lowest grade: {lowest_grade}")
print(f"Highest grade: {highest_grade}")
print(f"Sum of grades: {total_grades}")
print(f"Average grade: {average_grade:.2f}")
print("------------------------")
