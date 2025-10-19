import numpy as np
import matplotlib.pyplot as plt

# Define the logistic (sigmoid) function
def logistic(x, L=1, k=1, x0=0):
    """
    Logistic function:
    L  = curve's maximum value
    k  = steepness of the curve
    x0 = x-value of the sigmoid's midpoint
    """
    return L / (1 + np.exp(-k * (x - x0)))

# Example usage
x = np.linspace(-10, 10, 500)
y = logistic(x, L=1, k=1, x0=0)

# Plot the function
plt.plot(x, y)
plt.title("Logistic Function")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.show()
