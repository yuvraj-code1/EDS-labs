import pandas as pd
import matplotlib.pyplot as plt

# Load the Titanic dataset from the CSV file
df = pd.read_csv('titanic.csv')

# Set up the figure for 5 subplots
fig, axes = plt.subplots(3, 2, figsize=(12, 12))

# write the code..
pc=df['Pclass'].value_counts()
axes[0,0].bar(pc.index,pc.values,color='skyblue')
axes[0,0].set_xlabel('Pclass')
axes[0,0].set_ylabel('Count')
axes[0,0].set_title('Passenger Class Distribution')

gc=df['Gender'].value_counts()
axes[0,1].pie(gc,labels=gc.index,autopct='%1.1f%%',colors=['lightblue','lightcoral'])
axes[0,1].set_title('Gender Distribution')

axes[1,0].hist(df['Age'],bins=8,color='lightgreen',edgecolor='black')
axes[1,0].set_title("Age Distribution")
axes[1,0].set_xlabel('Age')
axes[1,0].set_ylabel('Frequency')

survival_counts=df['Survived'].value_counts()
axes[1,1].bar(survival_counts.index,survival_counts.values,color=['lightblue','lightcoral'])
axes[1,1].set_title('Survival Count')
axes[1,1].set_xlabel('Survived(0=No,2=Yes)')
axes[1,1].set_ylabel('Count')

axes[2,0].scatter(df['Age'],df['Fare'],color='orange')
axes[2,0].set_xlabel("Age")
axes[2,0].set_ylabel("Fare")
axes[2,0].set_title("Fare vs Age")
plt.tight_layout()

plt.show()