# Ask the user for the number of scores
num_scores = int(input("How many scores do you want to enter? "))
# This is a comment
# Tori Strickland
# 07/07/2024
# P4HW1
# Displaying scores and results

# Initialize an empty list to store scores
score_list = []

# Collect scores
for i in range(num_scores):
    score = float(input(f"Enter score #{i + 1}: "))
    while score < 0 or score > 100:
        print("INVALID Score entered!!!!")
        print("Score should be between 0 and 100")
        score = float(input(f"Enter score #{i + 1} again: "))
    score_list.append(score)

# Calculate the lowest score
lowest_score = min(score_list)

# Remove the lowest score from the list
score_list.remove(lowest_score)

# Calculate the average
average = sum(score_list) / len(score_list)

# Determine the letter grade
if average >= 90:
    letter_grade = "A"
elif average >= 80:
    letter_grade = "B"
elif average >= 70:
    letter_grade = "C"
else:
    letter_grade = "F"
print()
print()
print("----------Results----------")
# Display the results
print(f"Lowest Score: {lowest_score:.1f}")
print(f"Modified List: {score_list}")
print(f"Scores Average: {average:.2f}")
print(f"Letter Grade: {letter_grade}")
print("----------------------------")
