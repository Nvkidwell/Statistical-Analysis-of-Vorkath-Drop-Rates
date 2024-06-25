import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon, weibull_min, lognorm
from sklearn.metrics import mean_squared_error

# Given data
rarest_items = [
    {'Item': 'Dragonbone necklace', 'Rarity': 0.001},
    {'Item': 'Jar of decay', 'Rarity': 0.0003},
    {'Item': 'Vorki', 'Rarity': 0.0003},
    {'Item': 'Draconic visage', 'Rarity': 0.0005},
    {'Item': 'Skeletal visage', 'Rarity': 0.0005}
]

# Actual data for kills needed
actual_kills = {
    'Dragonbone necklace': 1000,
    'Jar of decay': 3000,
    'Vorki': 3000,
    'Draconic visage': 5000,
    'Skeletal visage': 5000
}

# Function to generate kills data
def generate_kills():
    return np.random.poisson(800, 1000)  # Generate Poisson-distributed kills

# Function to fit a probability distribution to the data and return the best fit
def fit_distribution(kills):
    # Fit distributions and select the best fit based on MSE
    dist_names = ['expon', 'weibull_min', 'lognorm']
    min_mse = float('inf')
    best_dist_name = None
    best_dist_params = None
    
    for dist_name in dist_names:
        if dist_name == 'expon':
            dist = expon.fit(kills)
        elif dist_name == 'weibull_min':
            dist = weibull_min.fit(kills, loc=0)
        elif dist_name == 'lognorm':
            dist = lognorm.fit(kills, loc=0)
        else:
            continue
        
        # Calculate PDF for each item
        pdf_values = {}
        for item, kill_count in actual_kills.items():
            pdf = getattr(eval(dist_name), 'pdf')(kill_count, *dist[:-2], loc=dist[-2], scale=dist[-1])
            pdf_values[item] = pdf
        
        # Calculate MSE against actual kill counts
        mse = mean_squared_error(list(actual_kills.values()), list(pdf_values.values()))
        
        # Update best fit
        if mse < min_mse:
            min_mse = mse
            best_dist_name = dist_name
            best_dist_params = dist
    
    return best_dist_name, best_dist_params

# Function to visualize the fitted distribution
def visualize_distribution(item_name, dist_name, dist_params):
    # Generate kills data (for demonstration)
    kills = generate_kills()
    
    # Fit distribution
    dist = getattr(eval(dist_name), 'rvs')(*dist_params[:-2], loc=dist_params[-2], scale=dist_params[-1])
    
    # Plot histogram of data
    plt.figure(figsize=(8, 6))
    plt.hist(kills, bins=20, density=True, alpha=0.7, color='blue', label='Actual Kills')

    # Plot fitted distribution PDF
    x = np.linspace(0, max(kills), 100)
    plt.plot(x, eval(dist_name).pdf(x, *dist_params[:-2], loc=dist_params[-2], scale=dist_params[-1]),
             color='red', lw=2, label=f'{dist_name} distribution')

    plt.title(f'Fitted Distribution for {item_name}')
    plt.xlabel('Number of Kills')
    plt.ylabel('Probability Density')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Example usage for each rare item
for item in rarest_items:
    item_name = item['Item']
    rarity = item['Rarity']
    
    # Fit distribution
    dist_name, dist_params = fit_distribution(generate_kills())
    
    # Visualize
    visualize_distribution(item_name, dist_name, dist_params)
