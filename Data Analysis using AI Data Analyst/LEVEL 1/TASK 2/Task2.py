import pandas as pd

# Load the CSV file (correct the filename)
file_path = "Data Analysis using AI Data Analyst\LEVEL 1\TASK 2\Dataset.csv" # Corrected filename (removed extra space)
data = pd.read_csv(file_path)

# ---- Descriptive Analysis ----

# 1. Basic statistical measures for numerical columns
numerical_stats = data.describe()

# Display numerical stats
print("Basic Statistical Measures (Numerical Columns):")
print(numerical_stats)

# 2. Distribution of categorical variables

# Country Code distribution (Top 10)
country_code_distribution = data['Country Code'].value_counts().head(10)

# City distribution (Top 10)
city_distribution = data['City'].value_counts().head(10)

# Cuisines distribution (Top 10, individual cuisines)
cuisines_split = data['Cuisines'].dropna().str.split(',', expand=True).stack()
cuisine_distribution = cuisines_split.str.strip().value_counts().head(10)

# Display categorical distributions
print("\nTop 10 Country Codes by Number of Restaurants:")
print(country_code_distribution)

print("\nTop 10 Cities by Number of Restaurants:")
print(city_distribution)

print("\nTop 10 Cuisines by Number of Restaurants:")
print(cuisine_distribution)
