def calculate_financial_health(income, total_expenses, savings):

    # Calculate savings and expense percentages
    savings_percentage = (savings / income) * 100
    expense_percentage = (total_expenses / income) * 100

    # Emergency fund target = 3 months of expenses
    emergency_fund_target = total_expenses * 3

    if savings >= emergency_fund_target:
        emergency_status = "Good"
    elif savings >= total_expenses:
        emergency_status = "Moderate"
    else:
        emergency_status = "Needs Improvement"

    # Savings score
    savings_score = min(savings_percentage * 2, 60)

    # Expense score
    if expense_percentage <= 50:
        expense_score = 30
    elif expense_percentage <= 70:
        expense_score = 20
    elif expense_percentage <= 85:
        expense_score = 10
    else:
        expense_score = 0

    # Emergency fund score
    if emergency_status == "Good":
        emergency_score = 10
    elif emergency_status == "Moderate":
        emergency_score = 5
    else:
        emergency_score = 0

    # Final health score
    health_score = savings_score + expense_score + emergency_score

    # Keep score between 0 and 100
    health_score = max(0, min(100, health_score))

    # Financial status
    if health_score >= 75:
        status = "Good"
    elif health_score >= 50:
        status = "Moderate"
    else:
        status = "Needs Improvement"

    return {
        "health_score": round(health_score, 2),
        "status": status,
        "savings_percentage": round(savings_percentage, 2),
        "expense_percentage": round(expense_percentage, 2),
        "emergency_fund_target": round(emergency_fund_target, 2),
        "emergency_status": emergency_status
    }


# Example user
income = 50000

expenses = {
    "rent": 12000,
    "food": 6000,
    "transport": 3000,
    "shopping": 4000,
    "entertainment": 2000,
    "other_expenses": 3000
}

# Calculate total expenses
total_expenses = sum(expenses.values())

# Calculate savings
savings = income - total_expenses

# Calculate financial health
result = calculate_financial_health(
    income,
    total_expenses,
    savings
)

print("================================")
print("     FINANCIAL HEALTH REPORT")
print("================================")
print(f"Monthly Income       : ₹{income}")
print(f"Total Expenses       : ₹{total_expenses}")
print(f"Monthly Savings      : ₹{savings}")
print(f"Savings Rate         : {result['savings_percentage']}%")
print(f"Expense Ratio        : {result['expense_percentage']}%")
print(f"Emergency Fund Goal  : ₹{result['emergency_fund_target']}")
print(f"Emergency Fund Status: {result['emergency_status']}")
print(f"Health Score         : {result['health_score']}/100")
print(f"Financial Status     : {result['status']}")
print("================================")