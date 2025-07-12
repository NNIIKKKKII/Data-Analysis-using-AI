import pandas as pd

# Load the dataset
# file_path = 'Dataset .csv'
file_path = "Data Analysis using AI Data Analyst\LEVEL 2\TASK 2\Dataset .csv" # Corrected filename (removed extra space)
data = pd.read_csv(file_path)

# Check if required columns exist
required_columns = ['Price range', 'Aggregate rating', 'Rating color']
if not all(col in data.columns for col in required_columns):
    raise ValueError("Dataset missing one or more required columns.")

# 1. Most common price range
most_common_price_range = data['Price range'].mode()[0]
print(f"Most Common Price Range: {most_common_price_range}")

# 2. Average rating for each price range
average_rating_by_price_range = data.groupby('Price range')['Aggregate rating'].mean()
print("\nAverage Rating by Price Range:")
print(average_rating_by_price_range)

# 3. Most common rating color for the highest average rating price range
highest_avg_rating_price_range = average_rating_by_price_range.idxmax()
most_common_rating_color = (
    data[data['Price range'] == highest_avg_rating_price_range]['Rating color']
    .mode()[0]
)

print(f"\nHighest Avg Rating Price Range: {highest_avg_rating_price_range}")
print(f"Most Common Rating Color for This Price Range: {most_common_rating_color}")
