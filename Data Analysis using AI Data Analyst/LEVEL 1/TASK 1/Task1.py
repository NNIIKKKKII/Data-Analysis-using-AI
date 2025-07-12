import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file (make sure the filename is correct)
file_path = "Data Analysis using AI Data Analyst\LEVEL 1\TASK 1\Dataset.csv" # Corrected filename (removed extra space)
data = pd.read_csv(file_path)

# Display the shape of the dataset
print("Dataset Shape:", data.shape)
# LEVEL 1\Dataset .csv
# Display the first few rows
print("\nFirst 5 rows of the dataset:")
print(data.head())

# Check for missing values in each column
missing_values = data.isnull().sum()
print("\nMissing values in each column:")
print(missing_values)

# Handle missing values in 'Cuisines' column (if present)
if 'Cuisines' in data.columns:
    data['Cuisines'].fillna('Unknown', inplace=True)

# Recheck for missing values after filling
print("\nMissing values after handling:")
print(data.isnull().sum())

# Check data types of each column
print("\nData types before conversion:")
print(data.dtypes)

# Convert categorical columns to 'category' data type if they exist
categorical_columns = [
    'Has Table booking', 'Has Online delivery',
    'Is delivering now', 'Switch to order menu'
]

for column in categorical_columns:
    if column in data.columns:
        data[column] = data[column].astype('category')

# Display updated data types
print("\nData types after conversion:")
print(data.dtypes)

# Analyze distribution of the target variable 'Aggregate rating'
if 'Aggregate rating' in data.columns:
    plt.figure(figsize=(10, 6))
    sns.histplot(data['Aggregate rating'], bins=20, kde=True)
    plt.title('Distribution of Aggregate Rating')
    plt.xlabel('Aggregate Rating')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()

    # Summary statistics
    rating_stats = data['Aggregate rating'].describe()
    print("\nSummary statistics of Aggregate Rating:")
    print(rating_stats)

    # Count plot to check class imbalance
    plt.figure(figsize=(10, 6))
    sns.countplot(x='Aggregate rating', data=data)
    plt.title('Count of Aggregate Ratings')
    plt.xlabel('Aggregate Rating')
    plt.ylabel('Count')
    plt.grid(True)
    plt.show()

    # Display class distribution
    print("\nClass distribution (%):")
    rating_counts = data['Aggregate rating'].value_counts(normalize=True) * 100
    print(rating_counts.sort_index())
else:
    print("Column 'Aggregate rating' not found in the dataset.")
