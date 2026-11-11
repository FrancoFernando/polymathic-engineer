from pathlib import Path

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load the salary dataset
data = np.genfromtxt(Path(__file__).with_name("Salary Data.csv"), delimiter=",", skip_header=1)
X = data[:, 0].reshape(-1, 1)
y = data[:, 1]

# Train the model
model = LinearRegression()
model.fit(X, y)

# The learned parameters
print(f"Weight: {model.coef_[0]:.2f}")
print(f"Bias: {model.intercept_:.2f}")

# Evaluate
predictions = model.predict(X)
print(f"MSE: {mean_squared_error(y, predictions):.2f}")
print(f"R-squared: {r2_score(y, predictions):.4f}")

# Predict salary for 4.5 years of experience
new_experience = np.array([[4.5]])
predicted_salary = model.predict(new_experience)
print(f"\nPredicted salary for 4.5 years: ${predicted_salary[0]:,.0f}")
