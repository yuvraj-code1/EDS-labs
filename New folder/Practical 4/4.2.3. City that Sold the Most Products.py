import pandas as pd

# Prompt the user for the file name
file_name = input()

# Load the data
df = pd.read_csv(file_name)

# write the code..
best_city = df.groupby('City')['Quantity'].sum().idxmax()
# Display the result
print(f"City sold the most products: {best_city}")


