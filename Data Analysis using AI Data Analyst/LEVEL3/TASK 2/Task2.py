import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = "Data Analysis using AI Data Analyst\LEVEL 3\TASK 2\Dataset.csv" # Corrected filename (removed extra space)
data = pd.read_csv(file_path)

# Drop rows with missing ratings
data = data.dropna(subset=['Aggregate rating'])

# ----------------------------- Distribution of Ratings -----------------------------

# Histogram
plt.figure(figsize=(10, 6))
sns.histplot(data['Aggregate rating'], bins=20, kde=True, color='skyblue')
plt.title('Distribution of Aggregate Ratings')
plt.xlabel('Aggregate Rating')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# Barplot (Count of each rating)
plt.figure(figsize=(10, 6))
sns.countplot(x='Aggregate rating', data=data, palette='viridis', order=sorted(data['Aggregate rating'].unique()))
plt.title('Count of Aggregate Ratings')
plt.xlabel('Aggregate Rating')
plt.ylabel('Count')
plt.grid(True)
plt.show()

# ----------------------------- Average Rating by Cuisine -----------------------------

# Handle cuisines with too many unique combinations by splitting and simplifying
# Extract only the first cuisine (most prominent) from multi-cuisine entries
data['Primary Cuisine'] = data['Cuisines'].dropna().apply(lambda x: x.split(',')[0])

# Plot top 15 cuisines by frequency
top_cuisines = data['Primary Cuisine'].value_counts().nlargest(15).index
filtered_data = data[data['Primary Cuisine'].isin(top_cuisines)]

plt.figure(figsize=(12, 6))
sns.barplot(x='Primary Cuisine', y='Aggregate rating', data=filtered_data, ci=None, palette='magma')
plt.title('Average Aggregate Rating by Top 15 Cuisines')
plt.xlabel('Cuisine')
plt.ylabel('Average Rating')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

# ----------------------------- Average Rating by City -----------------------------

# Handle missing or too many cities
top_cities = data['City'].value_counts().nlargest(15).index
filtered_city_data = data[data['City'].isin(top_cities)]

plt.figure(figsize=(12, 6))
sns.barplot(x='City', y='Aggregate rating', data=filtered_city_data, ci=None, palette='coolwarm')
plt.title('Average Aggregate Rating by Top 15 Cities')
plt.xlabel('City')
plt.ylabel('Average Rating')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

# ----------------------------- Correlation Heatmap -----------------------------

# Encode categorical variables for correlation
encoded = pd.get_dummies(data[['Has Table booking', 'Has Online delivery', 'Price range', 'Rating color']], drop_first=True)
numeric_data = pd.concat([data[['Aggregate rating']], encoded], axis=1)

# Plot correlation heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(numeric_data.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap of Features with Aggregate Rating')
plt.show()
