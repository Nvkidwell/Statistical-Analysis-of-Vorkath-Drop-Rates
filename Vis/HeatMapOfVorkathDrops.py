import numpy as np
from sklearn.linear_model import LinearRegression

# Given data
rarest_items = [
    {'Item': 'Dragonbone necklace', 'Rarity': 0.001},
    {'Item': 'Jar of decay', 'Rarity': 0.0003},
    {'Item': 'Vorki', 'Rarity': 0.0003},
    {'Item': 'Draconic visage', 'Rarity': 0.0005},
    {'Item': 'Skeletal visage', 'Rarity': 0.0005}
]

current_kill_count = 732

# Calculate the cumulative rarity for these items
total_rarity = sum(item['Rarity'] for item in rarest_items)

# Calculate the probability of not receiving any of these items after n kills
def probability_no_drop(kills):
    return (1 - sum(1 - item['Rarity'] for item in rarest_items) ** kills)

# Function to predict the number of kills required to reach a certain probability threshold
def predict_killcount_for_probability(probability_threshold):
    X = np.array([[1]])
    y = np.log(1 - probability_threshold) / np.log(1 - total_rarity)
    
    model = LinearRegression()
    model.fit(X, y)
    
    # Predict the number of kills
    kills_needed = np.ceil((model.predict([[1]])[0][0] - np.log(1 - total_rarity) * current_kill_count) / np.log(1 - total_rarity))
    
    return int(kills_needed)

# Predict the kill count needed to reach a 50% chance of receiving at least one item
probability_threshold = 0.5
kills_needed = predict_killcount_for_probability(probability_threshold)

print(f"To have a {probability_threshold * 100}% chance of receiving at least one rare item, you would need to kill approximately {kills_needed} times.")
