# Prompt the user for their monthly income and monthly expences

monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))

# Calculate Monthly Savings.
monthly_savings = monthly_income - monthly_expenses

# Project Annual Savings:
savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

# Print the results
print(f"Your monthly savings are ${monthly_savings}.")
print(f"Project savings after one year, with interest, is: ${savings}.")