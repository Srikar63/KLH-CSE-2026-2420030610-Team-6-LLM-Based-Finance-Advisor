import streamlit as st
import pandas as pd
import joblib
import plotly.express as px
import os
import sys
import re



PROJECT_ROOT = os.path.dirname(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

sys.path.insert(0, PROJECT_ROOT)


# =========================================================
# BACKEND IMPORTS
# =========================================================

from backend.finance_analysis import calculate_financial_health
from backend.budget_recommendation import get_budget_recommendations
from backend.investment_recommendation import get_investment_recommendation


# =========================================================
# MODEL
# =========================================================

MODEL_PATH = os.path.join(
    PROJECT_ROOT,
    "ml",
    "savings_model.pkl"
)

model = joblib.load(MODEL_PATH)


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="FinancePro",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# CSS
# =========================================================

st.markdown("""
<style>

@import url(
'https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap'
);

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: #f4f7fb;
}

.block-container {
    max-width: 1380px;
    padding-top: 25px;
    padding-bottom: 60px;
}


/* =====================================================
   SIDEBAR
   ===================================================== */

section[data-testid="stSidebar"] {
    background: #ffffff;
    border-right: 1px solid #e3e8ef;
}

section[data-testid="stSidebar"] > div {
    padding-top: 30px;
}

.sidebar-logo {
    color: #2563eb;
    font-size: 24px;
    font-weight: 800;
}

.sidebar-subtitle {
    color: #94a3b8;
    font-size: 11px;
    margin-top: 4px;
    margin-bottom: 30px;
}

.sidebar-heading {
    color: #94a3b8;
    font-size: 9px;
    font-weight: 800;
    letter-spacing: 1px;
    margin-top: 22px;
    margin-bottom: 7px;
}

section[data-testid="stSidebar"] .stButton {
    margin-bottom: 4px;
}

section[data-testid="stSidebar"] .stButton > button {
    background: transparent !important;
    color: #64748b !important;
    border: none !important;
    box-shadow: none !important;
    text-align: left !important;
    justify-content: flex-start !important;
    height: 42px !important;
    padding-left: 13px !important;
    font-size: 13px !important;
    font-weight: 500 !important;
    border-radius: 9px !important;
}

section[data-testid="stSidebar"] .stButton > button:hover {
    background: #eef4ff !important;
    color: #2563eb !important;
}


/* =====================================================
   HEADER
   ===================================================== */

.top-header {
    background: #ffffff;
    border: 1px solid #e3e8f0;
    border-radius: 15px;
    padding: 20px 25px;
    margin-bottom: 30px;
    box-shadow: 0 5px 18px rgba(15,23,42,0.04);
}

.top-title {
    color: #172554;
    font-size: 23px;
    font-weight: 800;
}

.top-subtitle {
    color: #64748b;
    font-size: 12px;
    margin-top: 4px;
}


/* =====================================================
   TITLES
   ===================================================== */

.page-title {
    color: #172554;
    font-size: 30px;
    font-weight: 800;
    margin-bottom: 5px;
}

.page-subtitle {
    color: #64748b;
    font-size: 13px;
    margin-bottom: 27px;
}

.section-title {
    color: #172554;
    font-size: 19px;
    font-weight: 800;
    margin-top: 20px;
    margin-bottom: 4px;
}

.section-subtitle {
    color: #94a3b8;
    font-size: 11px;
    margin-bottom: 15px;
}


/* =====================================================
   CARDS
   ===================================================== */

.card {
    background: #ffffff;
    border: 1px solid #e3e8f0;
    border-radius: 14px;
    padding: 20px;
    box-shadow: 0 5px 17px rgba(15,23,42,0.045);
}

.card-title {
    color: #172554;
    font-size: 16px;
    font-weight: 800;
    margin-bottom: 5px;
}

.card-subtitle {
    color: #94a3b8;
    font-size: 11px;
}


/* =====================================================
   INPUTS
   ===================================================== */

[data-testid="stWidgetLabel"] p {
    color: #172554 !important;
    font-weight: 700 !important;
    font-size: 13px !important;
}

[data-testid="stWidgetLabel"] {
    color: #172554 !important;
}

div[data-baseweb="input"] {
    background: #ffffff !important;
    border: 1px solid #d5dce8 !important;
    border-radius: 9px !important;
}

div[data-baseweb="input"] input {
    color: #172554 !important;
    font-weight: 600 !important;
    background: #ffffff !important;
}

div[data-baseweb="select"] {
    background: #ffffff !important;
    border-radius: 9px !important;
}

div[data-baseweb="select"] * {
    color: #172554 !important;
}

.field-description {
    color: #94a3b8;
    font-size: 10px;
    margin-top: -10px;
    margin-bottom: 13px;
    line-height: 1.4;
}


/* =====================================================
   METRIC CARDS
   ===================================================== */

.metric-card {
    background: #ffffff;
    border: 1px solid #e3e8f0;
    border-radius: 14px;
    padding: 18px;
    min-height: 118px;
    box-shadow: 0 5px 17px rgba(15,23,42,0.045);
}

.metric-label {
    color: #64748b;
    font-size: 10px;
    font-weight: 700;
    letter-spacing: .3px;
}

.metric-value {
    color: #172554;
    font-size: 23px;
    font-weight: 800;
    margin-top: 10px;
}

.metric-note {
    color: #94a3b8;
    font-size: 10px;
    margin-top: 4px;
}

.metric-blue {
    border-top: 4px solid #2563eb;
}

.metric-green {
    border-top: 4px solid #10b981;
}

.metric-orange {
    border-top: 4px solid #f59e0b;
}

.metric-purple {
    border-top: 4px solid #8b5cf6;
}


/* =====================================================
   PROGRESS
   ===================================================== */

.progress-background {
    width: 100%;
    height: 10px;
    background: #e8eef6;
    border-radius: 20px;
    overflow: hidden;
}

.progress-bar {
    height: 10px;
    background: linear-gradient(
        90deg,
        #2563eb,
        #6366f1
    );
    border-radius: 20px;
}


/* =====================================================
   STATUS
   ===================================================== */

.status-good {
    background: #ecfdf5;
    border: 1px solid #bbf7d0;
    color: #047857;
    padding: 13px;
    border-radius: 9px;
    font-size: 12px;
    font-weight: 700;
}

.status-moderate {
    background: #fffbeb;
    border: 1px solid #fde68a;
    color: #b45309;
    padding: 13px;
    border-radius: 9px;
    font-size: 12px;
    font-weight: 700;
}

.status-needs {
    background: #fff1f2;
    border: 1px solid #fecdd3;
    color: #be123c;
    padding: 13px;
    border-radius: 9px;
    font-size: 12px;
    font-weight: 700;
}


/* =====================================================
   RECOMMENDATIONS
   ===================================================== */

.recommendation {
    background: #f8fafc;
    border: 1px solid #e8edf4;
    border-left: 3px solid #4f46e5;
    border-radius: 8px;
    padding: 12px 14px;
    margin-bottom: 9px;
    color: #475569;
    font-size: 12px;
    line-height: 1.6;
}


/* =====================================================
   GUIDANCE
   ===================================================== */

.guidance-card {
    background: linear-gradient(
        135deg,
        #eff6ff,
        #f5f3ff
    );

    border: 1px solid #dbe4ff;
    border-radius: 14px;
    padding: 20px;

    color: #334155;
    font-size: 13px;
    line-height: 1.7;
}


/* =====================================================
   INVESTMENT INFO
   ===================================================== */

.risk-info {
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 12px;
    padding: 16px;
    margin-top: 5px;
    margin-bottom: 18px;
}

.risk-title {
    color: #172554;
    font-size: 13px;
    font-weight: 800;
    margin-bottom: 6px;
}

.risk-text {
    color: #64748b;
    font-size: 11px;
    line-height: 1.7;
}


/* =====================================================
   INFO BOX
   ===================================================== */

.info-box {
    background: #ffffff;
    border: 1px solid #e3e8f0;
    border-radius: 14px;
    padding: 22px;
    box-shadow: 0 5px 17px rgba(15,23,42,0.045);
    min-height: 180px;
}

.info-title {
    color: #172554;
    font-size: 17px;
    font-weight: 800;
    margin-bottom: 12px;
}

.info-text {
    color: #64748b;
    font-size: 12px;
    line-height: 1.8;
}


/* =====================================================
   FOOTER
   ===================================================== */

.footer {
    text-align: center;
    color: #94a3b8;
    font-size: 10px;
    margin-top: 50px;
    padding-top: 20px;
    border-top: 1px solid #e2e8f0;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# SESSION STATE
# =========================================================

if "page" not in st.session_state:
    st.session_state.page = "Dashboard"

if "finance" not in st.session_state:
    st.session_state.finance = None


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.html("""
        <div class="sidebar-logo">
            💰 FinancePro
        </div>

        <div class="sidebar-subtitle">
            Personal Finance Advisor
        </div>

        <div class="sidebar-heading">
            MAIN MENU
        </div>
    """)

    if st.button("📊  Dashboard", use_container_width=True):
        st.session_state.page = "Dashboard"
        st.rerun()

    if st.button("💳  Spending", use_container_width=True):
        st.session_state.page = "Spending"
        st.rerun()

    if st.button("💰  Savings", use_container_width=True):
        st.session_state.page = "Savings"
        st.rerun()

    if st.button("📈  Investments", use_container_width=True):
        st.session_state.page = "Investments"
        st.rerun()

    st.html("""
        <div class="sidebar-heading">
            ANALYSIS
        </div>
    """)

    if st.button("📋  Financial Report", use_container_width=True):
        st.session_state.page = "Financial Report"
        st.rerun()

    if st.button("🎯  Financial Goals", use_container_width=True):
        st.session_state.page = "Financial Goals"
        st.rerun()

    st.html("""
        <div class="sidebar-heading">
            INFORMATION
        </div>
    """)

    if st.button("ℹ️  About Project", use_container_width=True):
        st.session_state.page = "About Project"
        st.rerun()


# =========================================================
# HEADER
# =========================================================

st.html("""
    <div class="top-header">

        <div class="top-title">
            Financial Dashboard
        </div>

        <div class="top-subtitle">
            Personal financial planning and analysis
        </div>

    </div>
""")


# =========================================================
# DASHBOARD
# =========================================================

if st.session_state.page == "Dashboard":

    st.html("""
        <div class="page-title">
            Welcome to your financial dashboard
        </div>

        <div class="page-subtitle">
            Plan your monthly finances, understand your spending,
            and make informed financial decisions.
        </div>
    """)


    # =====================================================
    # INPUT SECTION
    # =====================================================

    st.html("""
        <div class="card">

            <div class="card-title">
                Monthly Financial Details
            </div>

            <div class="card-subtitle">
                Enter your income, regular expenses and investment
                risk profile to generate your financial analysis.
            </div>

        </div>
    """)

    st.markdown("<br>", unsafe_allow_html=True)


    left, right = st.columns(2, gap="large")


    # =====================================================
    # LEFT SIDE
    # =====================================================

    with left:

        income = st.number_input(
            "Monthly Income (₹)",
            min_value=0,
            value=50000,
            step=1000
        )

        st.html("""
            <div class="field-description">
                Your total income received every month.
            </div>
        """)


        rent = st.number_input(
            "Rent (₹)",
            min_value=0,
            value=12000,
            step=500
        )

        st.html("""
            <div class="field-description">
                Monthly house, room or accommodation rent.
            </div>
        """)


        food = st.number_input(
            "Food (₹)",
            min_value=0,
            value=6000,
            step=500
        )

        st.html("""
            <div class="field-description">
                Monthly groceries, food and dining expenses.
            </div>
        """)


        transport = st.number_input(
            "Transport (₹)",
            min_value=0,
            value=3000,
            step=500
        )

        st.html("""
            <div class="field-description">
                Travel, fuel, public transport and commuting costs.
            </div>
        """)


    # =====================================================
    # RIGHT SIDE
    # =====================================================

    with right:

        shopping = st.number_input(
            "Shopping (₹)",
            min_value=0,
            value=4000,
            step=500
        )

        st.html("""
            <div class="field-description">
                Clothes, gadgets and other personal purchases.
            </div>
        """)


        entertainment = st.number_input(
            "Entertainment (₹)",
            min_value=0,
            value=2000,
            step=500
        )

        st.html("""
            <div class="field-description">
                Movies, games, outings and leisure activities.
            </div>
        """)


        other_expenses = st.number_input(
            "Other Expenses (₹)",
            min_value=0,
            value=3000,
            step=500
        )

        st.html("""
            <div class="field-description">
                Bills, subscriptions and other miscellaneous expenses.
            </div>
        """)


        # =================================================
        # IMPROVED RISK PROFILE
        # =================================================

        risk_profile = st.selectbox(
            "Investment Risk Profile",
            [
                "Low",
                "Moderate",
                "High"
            ]
        )


        if risk_profile == "Low":

            st.info(
                "🛡️ Low Risk: Focus on capital protection and "
                "stable options such as bank FDs, government "
                "securities, PPF and savings accounts."
            )

        elif risk_profile == "Moderate":

            st.info(
                "⚖️ Moderate Risk: Combine lower-risk savings "
                "with diversified market-linked investments "
                "for long-term growth."
            )

        else:

            st.warning(
                "📈 High Risk: Market-linked investments can "
                "experience significant fluctuations. Use only "
                "money that you can keep invested for the long term."
            )


        st.html("""
            <div class="field-description">
                Select how much investment risk you are comfortable taking.
            </div>
        """)


    st.markdown("<br>", unsafe_allow_html=True)


    analyze = st.button(
        "Analyze My Finances",
        use_container_width=True
    )


    # =====================================================
    # ANALYSIS
    # =====================================================

    if analyze:

        if income <= 0:

            st.error(
                "Please enter a valid monthly income."
            )

            st.stop()


        total_expenses = (
            rent
            + food
            + transport
            + shopping
            + entertainment
            + other_expenses
        )


        actual_savings = (
            income - total_expenses
        )


        # -------------------------------------------------
        # Prevent negative savings from creating confusion
        # -------------------------------------------------

        savings_for_analysis = max(
            0,
            actual_savings
        )


        user_data = pd.DataFrame(
            [{
                "income": income,
                "rent": rent,
                "food": food,
                "transport": transport,
                "shopping": shopping,
                "entertainment": entertainment,
                "other_expenses": other_expenses
            }]
        )


        # =================================================
        # XGBOOST PREDICTION
        # =================================================

        predicted_savings = model.predict(
            user_data
        )[0]

        predicted_savings = max(
            0,
            predicted_savings
        )


        # =================================================
        # FINANCIAL HEALTH
        # =================================================

        health_result = calculate_financial_health(
            income,
            total_expenses,
            savings_for_analysis
        )


        health_score = health_result["health_score"]
        status = health_result["status"]


        # =================================================
        # BUDGET RECOMMENDATIONS
        # =================================================

        expenses = {
            "rent": rent,
            "food": food,
            "transport": transport,
            "shopping": shopping,
            "entertainment": entertainment,
            "other_expenses": other_expenses
        }


        budget_advice = get_budget_recommendations(
            income,
            expenses
        )


        # =================================================
        # INVESTMENT RECOMMENDATIONS
        # =================================================

        investment_advice = get_investment_recommendation(
            predicted_savings,
            risk_profile,
            total_expenses
        )


        # =================================================
        # GEMINI GUIDANCE
        # =================================================

        guidance = (
            "Personalized AI guidance is temporarily unavailable."
        )


        try:

            from backend.llm_guidance import get_financial_guidance

            guidance = get_financial_guidance(
                predicted_savings,
                health_score,
                risk_profile
            )

        except Exception:

            guidance = (
                "AI guidance is temporarily unavailable. "
                "Your savings prediction, financial health "
                "and recommendations are still available."
            )


        # =================================================
        # SAVE RESULTS
        # =================================================

        st.session_state.finance = {

            "income": income,

            "rent": rent,

            "food": food,

            "transport": transport,

            "shopping": shopping,

            "entertainment": entertainment,

            "other_expenses": other_expenses,

            "total_expenses": total_expenses,

            "actual_savings": actual_savings,

            "predicted_savings": predicted_savings,

            "health_score": health_score,

            "status": status,

            "savings_percentage":
                health_result["savings_percentage"],

            "expense_percentage":
                health_result["expense_percentage"],

            "emergency_fund_target":
                health_result["emergency_fund_target"],

            "emergency_status":
                health_result["emergency_status"],

            "risk_profile": risk_profile,

            "budget_advice": budget_advice,

            "investment_advice": investment_advice,

            "guidance": guidance

        }


        st.success(
            "Financial analysis completed successfully."
        )


    # =====================================================
    # RESULTS
    # =====================================================

    if st.session_state.finance is not None:

        data = st.session_state.finance


        # =================================================
        # FINANCIAL OVERVIEW
        # =================================================

        st.html("""
            <div class="section-title">
                Financial Overview
            </div>

            <div class="section-subtitle">
                Key indicators from your monthly financial profile.
            </div>
        """)


        m1, m2, m3, m4 = st.columns(4)


        with m1:

            st.html(f"""
                <div class="metric-card metric-blue">

                    <div class="metric-label">
                        MONTHLY INCOME
                    </div>

                    <div class="metric-value">
                        ₹{data["income"]:,.0f}
                    </div>

                    <div class="metric-note">
                        Total monthly income
                    </div>

                </div>
            """)


        with m2:

            st.html(f"""
                <div class="metric-card metric-orange">

                    <div class="metric-label">
                        TOTAL EXPENSES
                    </div>

                    <div class="metric-value">
                        ₹{data["total_expenses"]:,.0f}
                    </div>

                    <div class="metric-note">
                        Monthly spending
                    </div>

                </div>
            """)


        with m3:

            st.html(f"""
                <div class="metric-card metric-green">

                    <div class="metric-label">
                        PREDICTED SAVINGS
                    </div>

                    <div class="metric-value">
                        ₹{data["predicted_savings"]:,.0f}
                    </div>

                    <div class="metric-note">
                        XGBoost prediction
                    </div>

                </div>
            """)


        with m4:

            st.html(f"""
                <div class="metric-card metric-purple">

                    <div class="metric-label">
                        FINANCIAL HEALTH
                    </div>

                    <div class="metric-value">
                        {data["health_score"]}/100
                    </div>

                    <div class="metric-note">
                        {data["status"]}
                    </div>

                </div>
            """)


        st.markdown("<br>", unsafe_allow_html=True)


        # =================================================
        # SAVINGS + STATUS
        # =================================================

        savings_col, status_col = st.columns(
            [1.25, 1],
            gap="large"
        )


        with savings_col:

            savings_rate = (
                data["actual_savings"]
                / data["income"]
            ) * 100

            savings_rate = max(
                0,
                min(100, savings_rate)
            )


            st.html(f"""
                <div class="card">

                    <div class="card-title">
                        Savings Progress
                    </div>

                    <div class="card-subtitle">
                        Current monthly savings rate.
                    </div>

                    <div style="
                        display:flex;
                        justify-content:space-between;
                        margin-top:18px;
                        margin-bottom:8px;
                        font-size:11px;
                    ">

                        <span style="color:#64748b;">
                            Savings rate
                        </span>

                        <strong style="color:#2563eb;">
                            {savings_rate:.1f}%
                        </strong>

                    </div>

                    <div class="progress-background">

                        <div
                            class="progress-bar"
                            style="width:{savings_rate}%"
                        >
                        </div>

                    </div>

                    <div style="
                        display:flex;
                        justify-content:space-between;
                        margin-top:14px;
                        color:#64748b;
                        font-size:11px;
                    ">

                        <span>
                            Actual savings
                        </span>

                        <strong style="color:#172554;">
                            ₹{data["actual_savings"]:,.0f}
                        </strong>

                    </div>

                </div>
            """)


        with status_col:

            if data["status"] == "Good":

                status_class = "status-good"

                message = (
                    "Your finances are in a healthy position."
                )

            elif data["status"] == "Moderate":

                status_class = "status-moderate"

                message = (
                    "Your finances are moderately healthy."
                )

            else:

                status_class = "status-needs"

                message = (
                    "Your finances may need improvement."
                )


            st.html(f"""
                <div class="card">

                    <div class="card-title">
                        Financial Status
                    </div>

                    <div class="card-subtitle">
                        Current financial health assessment.
                    </div>

                    <div class="{status_class}"
                         style="margin-top:18px;">
                        {message}
                    </div>

                    <div style="
                        display:flex;
                        justify-content:space-between;
                        margin-top:15px;
                        font-size:11px;
                        color:#64748b;
                    ">

                        <span>
                            Risk profile
                        </span>

                        <strong style="color:#172554;">
                            {data["risk_profile"]}
                        </strong>

                    </div>

                </div>
            """)


        # =================================================
        # FINANCIAL HEALTH DETAILS
        # =================================================

        st.html("""
            <div class="section-title">
                Financial Health Details
            </div>

            <div class="section-subtitle">
                Additional indicators calculated from your income,
                expenses and savings.
            </div>
        """)


        h1, h2, h3 = st.columns(3)


        with h1:

            st.metric(
                "Savings Percentage",
                f'{data["savings_percentage"]:.1f}%'
            )


        with h2:

            st.metric(
                "Expense Percentage",
                f'{data["expense_percentage"]:.1f}%'
            )


        with h3:

            st.metric(
                "Emergency Fund Target",
                f'₹{data["emergency_fund_target"]:,.0f}'
            )


        # =================================================
        # SPENDING ANALYSIS
        # =================================================

        st.html("""
            <div class="section-title">
                Spending Analysis
            </div>

            <div class="section-subtitle">
                Visual breakdown of your monthly expenses.
            </div>
        """)


        chart_data = pd.DataFrame(
            {
                "Category": [
                    "Rent",
                    "Food",
                    "Transport",
                    "Shopping",
                    "Entertainment",
                    "Other"
                ],

                "Amount": [
                    data["rent"],
                    data["food"],
                    data["transport"],
                    data["shopping"],
                    data["entertainment"],
                    data["other_expenses"]
                ]
            }
        )


        chart_col, donut_col = st.columns(
            [1.35, 1],
            gap="large"
        )


        with chart_col:

            st.html("""
                <div class="card-title">
                    Expense Breakdown
                </div>

                <div class="card-subtitle">
                    Monthly spending by category.
                </div>
            """)


            fig = px.bar(
                chart_data,
                x="Category",
                y="Amount",
                text_auto=".2s"
            )


            fig.update_traces(
                marker_color="#2563eb"
            )


            fig.update_layout(
                height=350,
                plot_bgcolor="white",
                paper_bgcolor="white",
                margin=dict(
                    l=10,
                    r=10,
                    t=20,
                    b=10
                ),
                xaxis_title="",
                yaxis_title="Amount (₹)",
                font=dict(
                    family="Inter",
                    color="#64748b"
                )
            )


            st.plotly_chart(
                fig,
                use_container_width=True
            )


        with donut_col:

            st.html("""
                <div class="card-title">
                    Spending Distribution
                </div>

                <div class="card-subtitle">
                    Share of total monthly expenses.
                </div>
            """)


            fig2 = px.pie(
                chart_data,
                names="Category",
                values="Amount",
                hole=0.58
            )


            fig2.update_layout(
                height=350,
                plot_bgcolor="white",
                paper_bgcolor="white",
                margin=dict(
                    l=10,
                    r=10,
                    t=20,
                    b=10
                ),
                font=dict(
                    family="Inter",
                    color="#64748b"
                )
            )


            st.plotly_chart(
                fig2,
                use_container_width=True
            )


        # =================================================
        # RECOMMENDATIONS
        # =================================================

        st.html("""
            <div class="section-title">
                Financial Recommendations
            </div>

            <div class="section-subtitle">
                Suggestions generated from your financial analysis.
            </div>
        """)


        budget_col, investment_col = st.columns(
            2,
            gap="large"
        )


        with budget_col:

            st.html("""
                <div class="card-title">
                    💳 Budget Recommendations
                </div>

                <div class="card-subtitle">
                    Suggestions based on your spending pattern.
                </div>
            """)


            if isinstance(data["budget_advice"], list):

                for advice in data["budget_advice"]:

                    st.html(f"""
                        <div class="recommendation">
                            • {advice}
                        </div>
                    """)

            else:

                st.html(f"""
                    <div class="recommendation">
                        • {data["budget_advice"]}
                    </div>
                """)


        with investment_col:

            st.html(f"""
                <div class="card-title">
                    📈 Investment Considerations
                </div>

                <div class="card-subtitle">
                    Based on your {data["risk_profile"].lower()} risk profile.
                </div>
            """)


            if isinstance(data["investment_advice"], list):

                for advice in data["investment_advice"]:

                    st.html(f"""
                        <div class="recommendation">
                            • {advice}
                        </div>
                    """)

            else:

                st.html(f"""
                    <div class="recommendation">
                        • {data["investment_advice"]}
                    </div>
                """)


        # =================================================
        # GEMINI GUIDANCE
        # =================================================

        st.html("""
            <div class="section-title">
                Personalized Financial Guidance
            </div>

            <div class="section-subtitle">
                Practical guidance based on your financial profile.
            </div>
        """)


        clean_guidance = str(
            data["guidance"]
        )


        clean_guidance = re.sub(
            r'#{1,6}\s*',
            '',
            clean_guidance
        )


        clean_guidance = clean_guidance.replace(
            "**",
            ""
        )


        lines = clean_guidance.splitlines()

        guidance_html = ""


        for line in lines:

            line = line.strip()

            if not line:
                continue

            if line.startswith("-"):
                line = line[1:].strip()

            if line.startswith("•"):
                line = line[1:].strip()


            guidance_html += f"""
                <div style="
                    margin-bottom:9px;
                    padding-left:4px;
                ">

                    <span style="
                        color:#4f46e5;
                        font-weight:800;
                        margin-right:7px;
                    ">
                        •
                    </span>

                    {line}

                </div>
            """


        st.html(f"""
            <div class="guidance-card">
                {guidance_html}
            </div>
        """)


# =========================================================
# SPENDING PAGE
# =========================================================

elif st.session_state.page == "Spending":

    st.html("""
        <div class="page-title">
            Spending Analysis
        </div>

        <div class="page-subtitle">
            Understand how your monthly income is being spent.
        </div>
    """)


    if st.session_state.finance is None:

        st.info(
            "Analyze your finances from the Dashboard first."
        )

    else:

        data = st.session_state.finance


        chart_data = pd.DataFrame(
            {
                "Category": [
                    "Rent",
                    "Food",
                    "Transport",
                    "Shopping",
                    "Entertainment",
                    "Other"
                ],

                "Amount": [
                    data["rent"],
                    data["food"],
                    data["transport"],
                    data["shopping"],
                    data["entertainment"],
                    data["other_expenses"]
                ]
            }
        )


        total = data["total_expenses"]


        c1, c2, c3 = st.columns(3)


        with c1:

            st.html(f"""
                <div class="metric-card metric-orange">

                    <div class="metric-label">
                        TOTAL SPENDING
                    </div>

                    <div class="metric-value">
                        ₹{total:,.0f}
                    </div>

                    <div class="metric-note">
                        Monthly expenses
                    </div>

                </div>
            """)


        with c2:

            highest = chart_data.loc[
                chart_data["Amount"].idxmax(),
                "Category"
            ]


            st.html(f"""
                <div class="metric-card metric-blue">

                    <div class="metric-label">
                        HIGHEST EXPENSE
                    </div>

                    <div class="metric-value">
                        {highest}
                    </div>

                    <div class="metric-note">
                        Largest spending category
                    </div>

                </div>
            """)


        with c3:

            expense_rate = (
                total / data["income"]
            ) * 100


            st.html(f"""
                <div class="metric-card metric-purple">

                    <div class="metric-label">
                        EXPENSE RATE
                    </div>

                    <div class="metric-value">
                        {expense_rate:.1f}%
                    </div>

                    <div class="metric-note">
                        Percentage of income
                    </div>

                </div>
            """)


        st.markdown("<br>", unsafe_allow_html=True)


        fig = px.bar(
            chart_data,
            x="Category",
            y="Amount",
            text_auto=".2s"
        )


        fig.update_traces(
            marker_color="#2563eb"
        )


        fig.update_layout(
            height=450,
            plot_bgcolor="white",
            paper_bgcolor="white",
            font=dict(
                family="Inter",
                color="#64748b"
            )
        )


        st.plotly_chart(
            fig,
            use_container_width=True
        )


# =========================================================
# SAVINGS PAGE
# =========================================================

elif st.session_state.page == "Savings":

    st.html("""
        <div class="page-title">
            Savings
        </div>

        <div class="page-subtitle">
            Track your current and predicted monthly savings.
        </div>
    """)


    if st.session_state.finance is None:

        st.info(
            "Analyze your finances from the Dashboard first."
        )

    else:

        data = st.session_state.finance


        savings_rate = (
            data["actual_savings"]
            / data["income"]
        ) * 100


        c1, c2, c3 = st.columns(3)


        with c1:

            st.html(f"""
                <div class="metric-card metric-green">

                    <div class="metric-label">
                        ACTUAL SAVINGS
                    </div>

                    <div class="metric-value">
                        ₹{data["actual_savings"]:,.0f}
                    </div>

                    <div class="metric-note">
                        Income minus expenses
                    </div>

                </div>
            """)


        with c2:

            st.html(f"""
                <div class="metric-card metric-blue">

                    <div class="metric-label">
                        PREDICTED SAVINGS
                    </div>

                    <div class="metric-value">
                        ₹{data["predicted_savings"]:,.0f}
                    </div>

                    <div class="metric-note">
                        XGBoost prediction
                    </div>

                </div>
            """)


        with c3:

            st.html(f"""
                <div class="metric-card metric-purple">

                    <div class="metric-label">
                        SAVINGS RATE
                    </div>

                    <div class="metric-value">
                        {savings_rate:.1f}%
                    </div>

                    <div class="metric-note">
                        Current savings percentage
                    </div>

                </div>
            """)


        st.markdown("<br>", unsafe_allow_html=True)


        st.html(f"""
            <div class="card">

                <div class="card-title">
                    Monthly Savings Progress
                </div>

                <div class="card-subtitle">
                    Your current savings compared with monthly income.
                </div>

                <div style="
                    margin-top:20px;
                    background:#e8eef6;
                    height:12px;
                    border-radius:20px;
                ">

                    <div style="
                        width:{max(0,min(100,savings_rate))}%;
                        height:12px;
                        border-radius:20px;
                        background:linear-gradient(
                            90deg,#2563eb,#6366f1
                        );
                    ">
                    </div>

                </div>

                <div style="
                    margin-top:15px;
                    color:#64748b;
                    font-size:12px;
                ">

                    You are currently saving

                    <b style="color:#172554;">
                        ₹{data["actual_savings"]:,.0f}
                    </b>

                    per month.

                </div>

            </div>
        """)


# =========================================================
# INVESTMENTS PAGE
# =========================================================

elif st.session_state.page == "Investments":

    st.html("""
        <div class="page-title">
            Investment Planning
        </div>

        <div class="page-subtitle">
            Investment considerations based on your selected risk profile.
        </div>
    """)


    if st.session_state.finance is None:

        st.info(
            "Analyze your finances from the Dashboard first."
        )

    else:

        data = st.session_state.finance


        # =================================================
        # RISK PROFILE
        # =================================================

        st.html(f"""
            <div class="card">

                <div class="card-title">
                    Investment Risk Profile
                </div>

                <div style="
                    font-size:27px;
                    font-weight:800;
                    color:#2563eb;
                    margin-top:10px;
                ">
                    {data["risk_profile"]}
                </div>

                <div class="card-subtitle"
                     style="margin-top:5px;">

                    Selected based on your comfort
                    with investment risk.

                </div>

            </div>
        """)


        st.markdown("<br>", unsafe_allow_html=True)


        # =================================================
        # DYNAMIC RISK INFORMATION
        # =================================================

        if data["risk_profile"] == "Low":

            st.html("""
                <div class="risk-info">

                    <div class="risk-title">
                        🛡️ Low-Risk Investment Approach
                    </div>

                    <div class="risk-text">

                        Your profile indicates that capital
                        protection and easy access to money
                        are important considerations.

                        <br><br>

                        Common options to research include:

                        <br>

                        • Bank Fixed Deposits (FDs)<br>
                        • Government Treasury Bills (T-Bills)<br>
                        • Public Provident Fund (PPF)<br>
                        • Savings Account for emergency money

                        <br><br>

                        Always check current interest rates,
                        lock-in periods, withdrawal rules and
                        applicable taxes before investing.

                    </div>

                </div>
            """)

        elif data["risk_profile"] == "Moderate":

            st.html("""
                <div class="risk-info">

                    <div class="risk-title">
                        ⚖️ Moderate-Risk Investment Approach
                    </div>

                    <div class="risk-text">

                        A moderate approach can combine
                        lower-risk products with diversified
                        market-linked investments.

                        <br><br>

                        Examples to research include:

                        <br>

                        • Fixed-income products<br>
                        • Government securities<br>
                        • Diversified mutual funds<br>
                        • Other suitable long-term investments

                        <br><br>

                        Market-linked investments can fluctuate
                        in value and should match your time horizon
                        and risk tolerance.

                    </div>

                </div>
            """)

        else:

            st.html("""
                <div class="risk-info">

                    <div class="risk-title">
                        📈 High-Risk Investment Approach
                    </div>

                    <div class="risk-text">

                        Higher-risk investments can experience
                        significant price fluctuations.

                        <br><br>

                        Areas to research may include:

                        <br>

                        • Equity investments<br>
                        • Diversified equity mutual funds<br>
                        • Long-term market-linked investments

                        <br><br>

                        Emergency money should generally be kept
                        separate from high-risk investments.

                    </div>

                </div>
            """)


        # =================================================
        # INVESTMENT RECOMMENDATIONS
        # =================================================

        st.html("""
            <div class="section-title">
                Investment Considerations
            </div>

            <div class="section-subtitle">
                General considerations generated from your
                savings and selected risk profile.
            </div>
        """)


        advice = data["investment_advice"]


        if isinstance(advice, list):

            for item in advice:

                st.html(f"""
                    <div class="recommendation">
                        📌 {item}
                    </div>
                """)

        else:

            st.html(f"""
                <div class="recommendation">
                    📌 {advice}
                </div>
            """)


        st.warning(
            "Investment information shown here is for educational "
            "purposes and is not professional financial advice. "
            "Investment values and returns can vary."
        )


# =========================================================
# FINANCIAL REPORT
# =========================================================

elif st.session_state.page == "Financial Report":

    st.html("""
        <div class="page-title">
            Financial Report
        </div>

        <div class="page-subtitle">
            Complete summary of your monthly financial analysis.
        </div>
    """)


    if st.session_state.finance is None:

        st.info(
            "Analyze your finances from the Dashboard first."
        )

    else:

        data = st.session_state.finance


        report = pd.DataFrame(
            {
                "Financial Metric": [
                    "Monthly Income",
                    "Total Expenses",
                    "Actual Savings",
                    "Predicted Savings",
                    "Financial Health Score",
                    "Financial Status",
                    "Investment Risk Profile",
                    "Emergency Fund Target"
                ],

                "Value": [
                    f'₹{data["income"]:,.0f}',
                    f'₹{data["total_expenses"]:,.0f}',
                    f'₹{data["actual_savings"]:,.0f}',
                    f'₹{data["predicted_savings"]:,.0f}',
                    f'{data["health_score"]}/100',
                    data["status"],
                    data["risk_profile"],
                    f'₹{data["emergency_fund_target"]:,.0f}'
                ]
            }
        )


        st.dataframe(
            report,
            use_container_width=True,
            hide_index=True
        )


        st.markdown("<br>", unsafe_allow_html=True)


        st.html(f"""
            <div class="card">

                <div class="card-title">
                    Financial Summary
                </div>

                <div class="card-subtitle"
                     style="margin-top:8px;">

                    Your monthly income is
                    <b>₹{data["income"]:,.0f}</b>.

                    Total expenses are
                    <b>₹{data["total_expenses"]:,.0f}</b>.

                    Your actual monthly savings are
                    <b>₹{data["actual_savings"]:,.0f}</b>.

                    The XGBoost model predicts approximately
                    <b>₹{data["predicted_savings"]:,.0f}</b>
                    in monthly savings.

                </div>

            </div>
        """)


# =========================================================
# FINANCIAL GOALS
# =========================================================

elif st.session_state.page == "Financial Goals":

    st.html("""
        <div class="page-title">
            Financial Goals
        </div>

        <div class="page-subtitle">
            Plan how long it may take to reach a savings target.
        </div>
    """)


    goal = st.number_input(
        "Target Amount (₹)",
        min_value=1000,
        value=100000,
        step=5000
    )


    st.html("""
        <div class="field-description">
            The amount you want to save for your financial goal.
        </div>
    """)


    monthly_saving = st.number_input(
        "Monthly Saving Amount (₹)",
        min_value=100,
        value=10000,
        step=500
    )


    st.html("""
        <div class="field-description">
            The amount you plan to save every month.
        </div>
    """)


    if monthly_saving > 0:

        months = goal / monthly_saving

        years = months / 12


        st.html(f"""
            <div class="card">

                <div class="card-title">
                    Goal Projection
                </div>

                <div class="card-subtitle">
                    Based on your selected monthly saving amount.
                </div>

                <div style="
                    display:grid;
                    grid-template-columns:1fr 1fr;
                    gap:20px;
                    margin-top:20px;
                ">

                    <div>

                        <div style="
                            color:#94a3b8;
                            font-size:10px;
                            font-weight:700;
                        ">
                            TARGET AMOUNT
                        </div>

                        <div style="
                            color:#172554;
                            font-size:22px;
                            font-weight:800;
                            margin-top:5px;
                        ">
                            ₹{goal:,.0f}
                        </div>

                    </div>


                    <div>

                        <div style="
                            color:#94a3b8;
                            font-size:10px;
                            font-weight:700;
                        ">
                            ESTIMATED TIME
                        </div>

                        <div style="
                            color:#2563eb;
                            font-size:22px;
                            font-weight:800;
                            margin-top:5px;
                        ">
                            {months:.1f} months
                        </div>

                    </div>

                </div>


                <div style="
                    color:#64748b;
                    font-size:12px;
                    margin-top:20px;
                ">

                    Approximately
                    <b>{years:.1f} years</b>
                    at
                    <b>₹{monthly_saving:,.0f}</b>
                    saved each month.

                </div>

            </div>
        """)


# =========================================================
# ABOUT PROJECT
# =========================================================

elif st.session_state.page == "About Project":

    st.html("""
        <div class="page-title">
            About FinancePro
        </div>

        <div class="page-subtitle">
            LLM-Based Intelligent Personal Finance Advisor
        </div>
    """)


    col1, col2 = st.columns(
        2,
        gap="large"
    )


    with col1:

        st.html("""
            <div class="info-box">

                <div class="info-title">
                    About the Project
                </div>

                <div class="info-text">

                    FinancePro is a personal finance analysis
                    application that helps users understand
                    their income, expenses and savings.

                    <br><br>

                    The system combines machine learning,
                    financial analysis rules and an LLM to
                    generate understandable financial guidance.

                </div>

            </div>
        """)


    with col2:

        st.html("""
            <div class="info-box">

                <div class="info-title">
                    Technologies Used
                </div>

                <div class="info-text">

                    • Python<br>
                    • Pandas & NumPy<br>
                    • Scikit-Learn<br>
                    • XGBoost<br>
                    • Streamlit<br>
                    • Plotly<br>
                    • Google Gemini API<br>
                    • Machine Learning<br>
                    • Large Language Model

                </div>

            </div>
        """)


    st.markdown("<br>", unsafe_allow_html=True)


    st.html("""
        <div class="info-box">

            <div class="info-title">
                How the System Works
            </div>

            <div class="info-text">

                <b>01</b> &nbsp;
                User enters monthly income and expenses.

                <br>

                <b>02</b> &nbsp;
                XGBoost predicts monthly savings.

                <br>

                <b>03</b> &nbsp;
                Financial health is calculated from
                income, expenses and savings.

                <br>

                <b>04</b> &nbsp;
                Spending and investment recommendations
                are generated according to the user's
                risk profile.

                <br>

                <b>05</b> &nbsp;
                Gemini provides concise natural-language
                financial guidance.

            </div>

        </div>
    """)


# =========================================================
# FOOTER
# =========================================================

st.html("""
    <div class="footer">

        FinancePro • Personal Finance Advisor

        <br>

        Intelligent Financial Planning Dashboard
        • Academic Project

    </div>
""")