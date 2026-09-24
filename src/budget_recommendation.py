def get_budget_recommendations(income, expenses):

    recommendations = []

    if income <= 0:
        return ["Please enter a valid income."]

    if expenses["rent"] > income * 0.30:
        recommendations.append("Rent is above 30% of income. Consider reducing housing costs.")

    if expenses["food"] > income * 0.15:
        recommendations.append("Food expenses are above 15% of income. Try to reduce unnecessary food spending.")

    if expenses["transport"] > income * 0.10:
        recommendations.append("Transport expenses are above 10% of income.")

    if expenses["shopping"] > income * 0.10:
        recommendations.append("Shopping expenses are high. Reduce unnecessary purchases.")

    if expenses["entertainment"] > income * 0.10:
        recommendations.append("Entertainment expenses are high. Consider setting a monthly limit.")

    if expenses["other_expenses"] > income * 0.10:
        recommendations.append("Other expenses are high. Review these expenses carefully.")

    if not recommendations:
        recommendations.append(
            "Your spending is within the recommended budget limits."
        )

    return recommendations