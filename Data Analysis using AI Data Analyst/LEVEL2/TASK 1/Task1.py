import pandas as pd

# Load the CSV file
file_path = "Data Analysis using AI Data Analyst\LEVEL 2\TASK 1\Dataset .csv" # Corrected filename (removed extra space)
data = pd.read_csv(file_path)

# -----------------------------
# 1. Percentage of Table Booking & Online Delivery
# -----------------------------

# Calculate the percentage of restaurants that offer table booking and online delivery
table_booking_percentage = data['Has Table booking'].value_counts(normalize=True) * 100
online_delivery_percentage = data['Has Online delivery'].value_counts(normalize=True) * 100

print("Percentage of Restaurants Offering Table Booking:")
print(table_booking_percentage.round(2))

print("\nPercentage of Restaurants Offering Online Delivery:")
print(online_delivery_percentage.round(2))

# -----------------------------
# 2. Compare Average Ratings Based on Table Booking
# -----------------------------

average_rating_table_booking = data.groupby('Has Table booking')['Aggregate rating'].mean()

print("\nAverage Ratings by Table Booking Availability:")
print(average_rating_table_booking.round(2))

# -----------------------------
# 3. Online Delivery Availability by Price Range
# -----------------------------

online_delivery_price_range = (
    data.groupby('Price range')['Has Online delivery']
    .value_counts(normalize=True)
    .unstack()
    * 100
)

print("\nOnline Delivery Availability by Price Range (in %):")
print(online_delivery_price_range.round(2))
