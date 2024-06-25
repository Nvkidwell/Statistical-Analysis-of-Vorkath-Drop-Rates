import matplotlib.pyplot as plt
import numpy as np

# Current in-game bond price
current_price = 14_000_000  # 14M gold per bond

# Estimated percentage increase over the next year (10-20%)
low_increase = 0.10  # 10%
high_increase = 0.20  # 20%

# Number of months to predict
months = np.arange(0, 13, 1)

# Calculate future prices
low_predicted_prices = current_price * (1 + low_increase) ** (months / 12)
high_predicted_prices = current_price * (1 + high_increase) ** (months / 12)

# Plot the predictions
plt.figure(figsize=(10, 6))
plt.plot(months, low_predicted_prices, label='10% Annual Increase', color='blue')
plt.plot(months, high_predicted_prices, label='20% Annual Increase', color='red')
plt.axhline(y=current_price, color='gray', linestyle='--', label='Current Price')

# Customize the plot
plt.title('Predicted In-Game Price of OSRS Bonds Over the Next Year')
plt.xlabel('Months')
plt.ylabel('In-Game Bond Price (in millions of gold)')
plt.legend()
plt.grid(True)
plt.xticks(months)
plt.yticks(np.arange(14_000_000, 17_000_000, 500_000), [f'{x/1_000_000:.1f}M' for x in np.arange(14_000_000, 17_000_000, 500_000)])
plt.show()
