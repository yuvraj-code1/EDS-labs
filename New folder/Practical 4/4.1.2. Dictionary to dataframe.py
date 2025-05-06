import pandas as pd

# Provided dictionary of lists
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
}

# Convert the dictionary to a DataFrame
df = pd.DataFrame(data)

# Display the original DataFrame
print("Original DataFrame:")
print(df)

# Adding a new row
new_name=input("New name: ")
new_age=int(input("New age: "))
new_row={'Name':new_name,'Age':new_age}
df=df.append(new_row,ignore_index=True)

# Display the DataFrame after adding a new row
print("After adding a row:\n",df)

# Modifying a row df.at[index,'Age']=new_age
index=int(input("Index of row to modify: "))
new_age=int(input("New age: "))
df.at[index,'Age']=new_age
# Display the DataFrame after modifying a row
print("After modifying a row:")
print(df)

# Deleting a row 
new_row_index=int(input("Index of row to delete: "))
df=df.drop(new_row_index).reset_index(drop=True)
# Display the DataFrame after deleting a row
print("After deleting a row:")
print(df)

# Adding a new column  
g=input("Enter genders separated by space: ").split()
df["Gender"]=g
# Display the DataFrame after adding a new column
print("After adding a new column:")
print(df)

# Modifying a column 

df["Name"]=df["Name"].str.upper()

# Display the DataFrame after modifying a column
print("After modifying a column:")
print(df)

# Deleting a column  
df=df.drop(columns='Age')
# Display the DataFrame after deleting a column
print("After deleting a column:")
print(df)
