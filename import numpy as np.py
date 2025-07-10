import numpy as np
from sklearn.linear_model import LinearRegression

# Example data
X = np.array([[1], [2], [3], [4], [5]])  # Features
y = np.array([2, 4, 5, 4, 5])           # Target

# Create and fit the model
model = LinearRegression()
model.fit(X, y)

# Predict
predictions = model.predict(X)
print("Predictions:", predictions)

# Coefficient and intercept
print("Slope:", model.coef_[0])
print("Intercept:", model.intercept_)