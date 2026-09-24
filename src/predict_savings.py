import joblib
import pandas as pd

# Load trained model
model = joblib.load("ml/savings_model.pkl")

# Example user
user_data = pd.DataFrame([{
    "income": 50000,
    "rent": 12000,
    "food": 6000,
    "transport": 3000,
    "shopping": 4000,
    "entertainment": 2000,
    "other_expenses": 3000
}])

# Predict savings
prediction = model.predict(user_data)[0]

print(f"Predicted Monthly Savings: ₹{prediction:.2f}")