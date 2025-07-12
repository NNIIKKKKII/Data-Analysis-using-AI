import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = "Data Analysis using AI Data Analyst\LEVEL 3\TASK 3\Dataset.csv" # Corrected filename (removed extra space)
data = pd.read_csv(file_path)

# ------------------ Distribution of Ratings ------------------

# Histogram of Aggregate Ratings
plt.figure(figsize=(10, 6))
sns.histplot(data['Aggregate rating'], bins=20, kde=True, color='skyblue')
plt.title('Distribution of Aggregate Ratings')
plt.xlabel('Aggregate Rating')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# Bar plot of Aggregate Ratings (Counts)
plt.figure(figsize=(10, 6))
sns.countplot(x='Aggregate rating', data=data, palette='viridis')
plt.title('Count of Aggregate Ratings')
plt.xlabel('Aggregate Rating')
plt.ylabel('Count')
plt.grid(True)
plt.show()

# ------------------ Average Ratings by Cuisine ------------------

# Extract first cuisine from the string (to simplify analysis)
data['Primary Cuisine'] = data['Cuisines'].astype(str).str.split(',').str[0]

# Bar plot for average ratings by primary cuisine
plt.figure(figsize=(14, 6))
avg_cuisine = data.groupby('Primary Cuisine')['Aggregate rating'].mean().sort_values(ascending=False).head(15)
sns.barplot(x=avg_cuisine.index, y=avg_cuisine.values, palette='magma')
plt.title('Top 15 Average Ratings by Cuisine')
plt.xlabel('Cuisine')
plt.ylabel('Average Rating')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# ------------------ Average Ratings by City ------------------

plt.figure(figsize=(14, 6))
avg_city = data.groupby('City')['Aggregate rating'].mean().sort_values(ascending=False).head(15)
sns.barplot(x=avg_city.index, y=avg_city.values, palette='coolwarm')
plt.title('Top 15 Average Ratings by City')
plt.xlabel('City')
plt.ylabel('Average Rating')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# ------------------ Relationships with Target Variable ------------------

# Average Cost for Two vs Aggregate Rating
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Average Cost for two', y='Aggregate rating', data=data, alpha=0.6, color='green')
plt.title('Average Cost for Two vs Aggregate Rating')
plt.xlabel('Average Cost for Two')
plt.ylabel('Aggregate Rating')
plt.grid(True)
plt.show()

# Votes vs Aggregate Rating
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Votes', y='Aggregate rating', data=data, alpha=0.6, color='purple')
plt.title('Votes vs Aggregate Rating')
plt.xlabel('Votes')
plt.ylabel('Aggregate Rating')
plt.grid(True)
plt.show()
