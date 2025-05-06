import pandas as pd

# Prompt the user for the file name
file_name = input()

# Load the data
df = pd.read_csv(file_name)
df["Total sales"] = df['Quantity'] * df['Price']


df['Date'] = pd.to_datetime(df["Date"])


df['Month'] = df['Date'].dt.to_period('M')

# Find the month with the highest total sales
monthly_sales = df.groupby('Month')['Total sales'].sum()

best_month = monthly_sales.idxmax()
highest_sales = monthly_sales.max()

print(f"Best month: {best_month}")
print(f"Total sales: ${highest_sales:.2f}")


