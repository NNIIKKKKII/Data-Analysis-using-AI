import pandas as pd
import folium
from folium.plugins import MarkerCluster
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
file_path = "Data Analysis using AI Data Analyst\LEVEL 1\TASK 3\Dataset.csv" # Corrected filename (removed extra space)
data = pd.read_csv(file_path)

# Drop rows with missing coordinates
data = data.dropna(subset=['Latitude', 'Longitude'])

# Create base map centered on average location
map_center = [data['Latitude'].mean(), data['Longitude'].mean()]
restaurant_map = folium.Map(location=map_center, zoom_start=2)

# Create a marker cluster
marker_cluster = MarkerCluster().add_to(restaurant_map)

# Add restaurant markers to the cluster
for idx, row in data.iterrows():
    name = row.get('Restaurant Name', 'Unnamed')
    rating = row.get('Aggregate rating', 'N/A')
    city = row.get('City', 'Unknown')
    popup_text = f"{name}<br>Rating: {rating}<br>City: {city}"
    folium.Marker(
        location=[row['Latitude'], row['Longitude']],
        popup=popup_text
    ).add_to(marker_cluster)

# Save the map to an HTML file
map_file_path = 'restaurant_map.html'
restaurant_map.save(map_file_path)

print(f"Map saved to: {map_file_path}")

# ---- ANALYSIS: Rating distribution by city or country ----

# Group by Country Code and calculate average rating
if 'Country Code' in data.columns:
    country_ratings = data.groupby('Country Code')['Aggregate rating'].mean().sort_values(ascending=False).head(10)
    plt.figure(figsize=(10,6))
    sns.barplot(x=country_ratings.index.astype(str), y=country_ratings.values)
    plt.title("Top 10 Countries by Average Aggregate Rating")
    plt.xlabel("Country Code")
    plt.ylabel("Average Rating")
    plt.show()

# Group by City and calculate average rating
if 'City' in data.columns:
    city_ratings = data.groupby('City')['Aggregate rating'].mean().sort_values(ascending=False).head(10)
    plt.figure(figsize=(10,6))
    sns.barplot(y=city_ratings.index, x=city_ratings.values)
    plt.title("Top 10 Cities by Average Aggregate Rating")
    plt.xlabel("Average Rating")
    plt.ylabel("City")
    plt.show()
