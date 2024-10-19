import numpy as np
import matplotlib.pyplot as plt

# Data
hours = np.array([1, 1, 1.5, 2, 2.5, 2.5, 2.5, 3, 3.5, 3.5, 3.5, 4, 4.5])
scores = np.array([0.5, 1.5, 1, 1.5, 1.5, 2.5, 3, 2, 1.5, 2, 2.5, 2, 2.5])

# Regression lines
f1 = lambda x: 0 + 1 * x
f2 = lambda x: 0.5 + 0.5 * x
f3 = lambda x: 1 + 0.25 * x

# Plotting
plt.figure(figsize=(8, 6))
plt.scatter(hours, scores, color='blue', label='Data Points')

# Adding regression lines
x_vals = np.linspace(0.5, 5, 100)
plt.plot(x_vals, f1(x_vals), label="f1: y = 1x", color='red')
plt.plot(x_vals, f2(x_vals), label="f2: y = 0.5x + 0.5", color='green')
plt.plot(x_vals, f3(x_vals), label="f3: y = 0.25x + 1", color='orange')

# Labels and title
plt.xlabel('Preparation time (hours)')
plt.ylabel('Test score')
plt.title('Test Scores vs Preparation Time with Regression Lines')
plt.legend()
plt.grid(True)
# Prediction values
x_values = [2, 4]

# Predictions for each regression function
predictions_f1 = [f1(x) for x in x_values]
predictions_f2 = [f2(x) for x in x_values]
predictions_f3 = [f3(x) for x in x_values]

# Organizing the predictions in a readable format
predictions = {
    "x_values": x_values,
    "f1_predictions": predictions_f1,
    "f2_predictions": predictions_f2,
    "f3_predictions": predictions_f3
}

print(predictions)
# Show plot
#plt.show()
