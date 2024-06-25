import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


file_path = "C:\\Users\\nvkid\OneDrive\\Desktop\\Data Science Project\\CSV Outputs\\aggregated_data.csv"
data = pd.read_csv(file_path)

print(data.head())

# Extract relevant columns
X = data['Killcount'].values.reshape(-1, 1)  # Features (independent variable)
y = data['Total Drop Value'].values.reshape(-1, 1)  # Target (dependent variable)

#(80% training, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a linear regression object
model = LinearRegression()

# model using the training sets
model.fit(X_train, y_train)

# testing set predictions
y_pred = model.predict(X_test)

# Plot
plt.scatter(X_test, y_test, color='black')  # test data points
plt.plot(X_test, y_pred, color='blue', linewidth=3)  # regression line
plt.title('Linear Regression of Expected Values Per Drop')
plt.xlabel('Killcount')
plt.ylabel('Total Drop Value')
plt.show()

# Calculate correlation matrix
correlation_matrix = data.corr()

# Plot heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', square=True)
plt.title('Correlation Matrix Heatmap')
plt.show()

