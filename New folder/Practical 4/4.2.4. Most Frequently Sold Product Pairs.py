import pandas as pd
from itertools import combinations
from collections import Counter

# Prompt user to input the file name
file_name = input()

# Read data from the specified CSV file
df = pd.read_csv(file_name)

# write the code


# Output the most frequent product pairs
# Group by 'Date' to find transactions on the same day
grouped = df.groupby('Date')['Product'].apply(list)

# Create a list to hold all product combinations sold together
product_combinations = []

# Iterate over grouped products and find all combinations of products sold on the same day
for products in grouped:
    # Generate all unique pairs of products sold on the same day
    product_combinations.extend(combinations(sorted(set(products)), 2))

# Count the frequency of each combination
combination_counts = Counter(product_combinations)

# Find the maximum frequency
max_count = combination_counts.most_common(1)[0][1]

# Output the most frequent product pairs
for combo, count in combination_counts.items():
    if count == max_count:
        print(f"{combo[0]} and {combo[1]}: {count} times")