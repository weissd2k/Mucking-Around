import numpy as np

# Manually enter your data here
# Example: x = [1, 2, 3, 4, 5], y = [2, 4, 5, 4, 5]
x = [float(i) for i in input("Enter x values separated by commas: ").split(",")]
y = [float(i) for i in input("Enter y values separated by commas: ").split(",")]

# Convert to numpy arrays
x = np.array(x)
y = np.array(y)

# Calculate slope (m) and intercept (b)
m, b = np.polyfit(x, y, 1)

print(f"Slope (m): {m}")
print(f"Intercept (b): {b}")

# Predict y values
y_pred = m * x + b
print("Predicted y values:", y_pred)

# Optional: Calculate R^2
r2 = 1 - np.sum((y - y_pred)**2) / np.sum((y - np.mean(y))**2)
print(f"R^2: {r2}")