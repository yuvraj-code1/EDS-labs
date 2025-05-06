import pandas as pd
import numpy as np

# Load the Titanic dataset
data = pd.read_csv('Titanic-Dataset.csv')
data = pd.get_dummies(data, columns=['Embarked'], drop_first=True)
# 1. Get the number of survivors by gender
print(data[data['Survived'] == 1]['Sex'].value_counts())

# 2. Get the number of non-survivors by gender
print(data[data['Survived'] == 0]['Sex'].value_counts())

# 3. Get the number of survivors by Embarked_S
print(data[data['Survived'] == 1]['Embarked_S'].value_counts())

# 4. Get the number of non-survivors by Embarked_S
print(data[data['Survived'] == 0]['Embarked_S'].value_counts())

# 5. Calculate the percentage of children (Age < 18) who survived
children = data[data['Age'] < 18]
children_survived = children[children['Survived'] == 1].shape[0]
print(children_survived / len(children))

# 6. Calculate the percentage of adults (Age >= 18) who survived
adults = data[data['Age'] >= 18]
adults_survived = adults[adults['Survived'] == 1].shape[0]
print(adults_survived / len(adults))

# 7. Get the median age of survivors
print(data[data['Survived'] == 1]['Age'].median())

# 8. Get the median age of non-survivors
print(data[data['Survived'] == 0]['Age'].median())

# 9. Get the median fare of survivors
print(data[data['Survived'] == 1]['Fare'].median())

# 10. Get the median fare of non-survivors
print(data[data['Survived'] == 0]['Fare'].median())