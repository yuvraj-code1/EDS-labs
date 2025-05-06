import pandas as pd

# Read the text file into a DataFrame
file = input()
data = pd.read_csv(file, sep="\s+", header=None, names=["Name", "Age", "Grade"])


# write your code here.. 
print("First five rows:")
print(data.head())
avg_age=round(data['Age'].mean(),2)
print("Average age:",avg_age)

print("Students with a grade up to B")
print(data[data['Grade'] <= 'B'])