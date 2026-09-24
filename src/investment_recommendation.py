def get_investment_recommendation(
    savings,
    risk_profile,
    total_expenses=0
):

    recommendations = []

    

    if savings <= 0:

        recommendations.append(
            "Focus on improving your monthly savings before starting investments."
        )

        recommendations.append(
            "Review unnecessary expenses and create a monthly budget."
        )

        return recommendations


 

    emergency_fund_target = total_expenses * 3

    if total_expenses > 0 and savings < emergency_fund_target:

        recommendations.append(
            f"First build an emergency fund of about "
            f"₹{emergency_fund_target:,.0f} "
            "before taking higher investment risks."
        )

    else:

        recommendations.append(
            "Your current savings can support long-term investment planning."
        )


    

    if risk_profile == "Low":

        recommendations.append(
            "🏦 Bank Fixed Deposit (FD): Suitable for "
            "capital protection and predictable returns. "
            "Eligible bank deposits are covered by DICGC "
            "insurance up to ₹5 lakh per depositor per bank."
        )

        recommendations.append(
            "🏛️ Government Treasury Bills (T-Bills): "
            "Short-term Government of India securities "
            "designed for relatively low credit risk."
        )

        recommendations.append(
            "📘 Public Provident Fund (PPF): A government-backed "
            "long-term savings option with a 15-year tenure. "
            "It is more suitable for long-term goals than emergency money."
        )

        recommendations.append(
            "💰 Savings Account: Keep part of your money easily "
            "accessible for emergencies and short-term needs."
        )

        recommendations.append(
            "⚠️ Low risk does not mean zero risk. Check interest rates, "
            "lock-in periods, withdrawal rules and applicable taxes before investing."
        )


  

    elif risk_profile == "Moderate":

        recommendations.append(
            "🏦 Keep your emergency fund in savings accounts or "
            "suitable fixed-income products."
        )

        recommendations.append(
            "📊 Consider diversified mutual funds for long-term "
            "growth if you are comfortable with market fluctuations."
        )

        recommendations.append(
            "🏛️ Government securities can be considered for the "
            "lower-risk portion of your portfolio."
        )

        recommendations.append(
            "⚖️ Maintain diversification instead of putting all "
            "your savings into one investment."
        )

        recommendations.append(
            "⚠️ Mutual funds and market-linked investments can lose value."
        )


   

    elif risk_profile == "High":

        recommendations.append(
            "📈 Equity-oriented investments may provide higher "
            "long-term growth potential but can fluctuate significantly."
        )

        recommendations.append(
            "📊 Diversified equity mutual funds can be considered "
            "for long-term goals if they match your risk tolerance."
        )

        recommendations.append(
            "🏦 Keep an emergency fund separate from high-risk investments."
        )

        recommendations.append(
            "⚠️ Higher potential returns come with higher market risk. "
            "Do not invest money needed for short-term expenses."
        )


   

    else:

        recommendations.append(
            "Please select Low, Moderate, or High risk profile."
        )


    return recommendations