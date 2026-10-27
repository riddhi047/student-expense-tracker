food = float(input("Enter food expenses: ₹"))
travel = float(input("Enter travel expenses: ₹"))
other = float(input("Enter other expenses: ₹"))

total = food + travel + other

print("Your total expenses are: ₹", total)
print("Average expense: ₹", total / 3)