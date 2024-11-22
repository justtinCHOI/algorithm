import numpy as np
import matplotlib.pyplot as plt

# Generate synthetic data
np.random.seed(42)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)  # y = 4 + 3x + noise

# Function to implement gradient descent
def gradient_descent(X, y, learning_rate=0.01, iterations=1000):
    m = len(y)
    X_b = np.c_[np.ones((m, 1)), X]  # Add bias term
    theta = np.random.randn(2, 1)  # Initialize random weights
    for iteration in range(iterations):
        gradients = 2/m * X_b.T.dot(X_b.dot(theta) - y)
        theta -= learning_rate * gradients
    return theta

# Apply gradient descent
theta = gradient_descent(X, y)

# Predict values
X_new = np.array([[0], [2]])
X_new_b = np.c_[np.ones((2, 1)), X_new]  # Add bias term
y_predict = X_new_b.dot(theta)

# Plot the data and the regression line
plt.figure(figsize=(10, 6))
plt.scatter(X, y, label='Data Points', alpha=0.8)
plt.plot(X_new, y_predict, color='red', label='Prediction (Regression Line)')
plt.title("Linear Regression using Gradient Descent")
plt.xlabel("X")
plt.ylabel("y")
plt.legend()
plt.grid()
plt.show()
