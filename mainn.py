import pandas as pd
import matplotlib.pyplot as plt

# Import the CSV file
data = pd.read_csv("Impact of gaming on life performance .csv")

# Data preprocessing
data = data.dropna()

# Descriptive statistics
gpa_mean = data['What is your GPA'].mean()
gpa_median = data['What is your GPA'].median()
gpa_std = data['What is your GPA'].std()

# Modify the column name or adjust it according to your data
influence_mean = data['influenced on problem-solving skills'].mean()
influence_std = data['influenced on problem-solving skills'].std()
decline_counts = data['decline in academic/work performance'].value_counts()

negative_effects_counts = data['negative effects on social interactions and relationships?'].value_counts()

positive_impacts_counts = data['positive impacts of gaming'].value_counts()

impact_mean = data['Impact Level'].mean()
impact_std = data['Impact Level'].std()

# Data visualization

plt.figure(figsize=(8, 6))
plt.hist(data['What is your GPA'], bins=10, edgecolor='black', range=(0, 4))  # Assuming GPA ranges from 0 to 4
plt.xlabel('GPA')
plt.ylabel('Frequency')
plt.title('GPA Distribution')
plt.show()

plt.figure(figsize=(8, 6))
plt.hist(data['influenced on problem-solving skills'], bins=5, edgecolor='black', range=(1, 6))  # Assuming ratings from 1 to 5
plt.xlabel('Rating')
plt.ylabel('Frequency')
plt.title('Influence on Problem-Solving Skills and Cognitive Abilities')
plt.xticks(range(1, 6))
plt.show()

decline_counts = data['decline in academic/work performance'].value_counts()
plt.figure(figsize=(8, 6))
plt.pie(decline_counts, labels=decline_counts.index, autopct='%1.1f%%')
plt.title('Decline in Academic/Work Performance')
plt.show()

negative_effects_counts = data['negative effects on social interactions and relationships?'].value_counts()
plt.figure(figsize=(8, 6))
plt.pie(negative_effects_counts, labels=negative_effects_counts.index, autopct='%1.1f%%')
plt.title('Negative Effects on Social Interactions and Relationships')
plt.show()

positive_impacts_counts = data['positive impacts of gaming'].value_counts()
plt.figure(figsize=(8, 6))
plt.pie(positive_impacts_counts, labels=positive_impacts_counts.index, autopct='%1.1f%%')
plt.title('Positive Impacts on Overall Well-being')
plt.show()

plt.figure(figsize=(8, 6))
plt.hist(data['Impact Level'], bins=5, edgecolor='black', range=(1, 6))  # Assuming ratings from 1 to 5
plt.xlabel('Rating')
plt.ylabel('Frequency')
plt.title('Overall Impact on Life Performance')
plt.xticks(range(1, 6))
plt.show()

# Print descriptive statistics
print("Descriptive Statistics:")
print("Question 1 - GPA:")
print("Mean: ", gpa_mean)
print("Median: ", gpa_median)
print("Standard Deviation: ", gpa_std)
print()

print("Question 2 - Influence on Problem-Solving Skills and Cognitive Abilities:")
print("Mean: ", influence_mean)
print("Standard Deviation: ", influence_std)
print()

print("Question 3 - Decline in Academic/Work Performance:")
print(decline_counts)
print()

print("Question 4 - Negative Effects on Social Interactions and Relationships:")
print(negative_effects_counts)
print()

print("Question 5 - Positive Impacts on Overall Well-being:")
print(positive_impacts_counts)
print()

print("Question 6 - Overall Impact on Life Performance:")
print("Mean: ", impact_mean)
