from pathlib import Path

import numpy as np

# Load the salary dataset
data = np.genfromtxt(Path(__file__).with_name("Salary Data.csv"), delimiter=",", skip_header=1)
X = data[:, 0]
y = data[:, 1]

# Normalize features to help gradient descent converge
X_mean, X_std = X.mean(), X.std()
y_mean, y_std = y.mean(), y.std()
X_norm = (X - X_mean) / X_std
y_norm = (y - y_mean) / y_std

# Initialize weight and bias to zero
weight = 0.0
bias = 0.0

# Hyperparameters
learning_rate = 0.01
epochs = 1000

# Gradient descent on normalized data
for epoch in range(epochs):
    predictions = weight * X_norm + bias
    errors = predictions - y_norm

    # Compute gradients
    weight_gradient = (2 / len(X_norm)) * np.dot(errors, X_norm)
    bias_gradient = (2 / len(X_norm)) * np.sum(errors)

    # Update weight and bias
    weight -= learning_rate * weight_gradient
    bias -= learning_rate * bias_gradient

    if epoch % 200 == 0:
        mse = np.mean(errors ** 2)
        print(f"Epoch {epoch}: MSE = {mse:.4f}, weight = {weight:.4f}, bias = {bias:.4f}")

# Convert back to original scale
real_weight = weight * y_std / X_std
real_bias = y_mean + y_std * bias - real_weight * X_mean

print(f"\nLearned equation: Salary = {real_weight:.2f} * experience + {real_bias:.2f}")

# Predict salary for 4.5 years of experience
new_experience = 4.5
predicted_salary = real_weight * new_experience + real_bias
print(f"Predicted salary for {new_experience} years: ${predicted_salary:,.0f}")
