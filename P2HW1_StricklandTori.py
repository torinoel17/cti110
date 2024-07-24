# This is a comment.
print("Tori Strickland")
print("06/20/2024")
print("P2HW1")
print("Calculating and displaying travel expenses")
print()
print("This program calculates and displays travel expenses")
print()
budget = float(input("Enter Budget: "))
print()
destination = input("Enter your travel destination:  ")
print()
gas_expenses = float(input("How much do you think you will spend on gas?  "))
print()
accomodation_expenses = float(input("Approximately, how much will you need for accomodation/hotel?  "))
print()
food_expenses = float(input("Last, how much do you need for food?  "))
print()
print('----------Travel Expenses----------')
print(f"Location:           {destination}")
print(f"Initial Budget:     ${budget:.2f}")
print(f"Fuel:               ${gas_expenses:.2f}")
print(f"Accommodation:      ${accomodation_expenses:.2f}")
print(f"Food:               ${food_expenses:.2f}")
print('------------------------------------')
total_expenses = gas_expenses + accomodation_expenses + food_expenses
remaining_balance = budget - total_expenses
print()
print(f"Remaining Balance: ${remaining_balance:.2f}")











                      
