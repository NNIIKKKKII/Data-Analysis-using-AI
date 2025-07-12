# 📊 Price Range Analysis of Restaurants

This project performs a descriptive analysis of restaurant data to explore how **price ranges** relate to **customer ratings** and **rating colors**.

---

## 🔍 Objective

The main goals of this analysis are:

1. **Identify the most common price range** among all restaurants.
2. **Calculate the average aggregate rating** for each price range.
3. **Determine the most common rating color** associated with the **highest-rated price range**.

---

## 📁 Dataset

The dataset used is `Dataset .csv`, which should contain at least the following columns:

- `Price range`: Indicates the pricing category (e.g., 1 to 4).
- `Aggregate rating`: Customer rating for the restaurant.
- `Rating color`: Visual color indicator for the rating level.

---

## 🧪 Steps Performed

1. **Load the Dataset**:
   - Uses `pandas` to read the dataset into a DataFrame.

2. **Find Most Common Price Range**:
   - Uses `mode()` to determine the most frequently occurring price range.

3. **Calculate Average Rating for Each Price Range**:
   - Groups data by `Price range` and calculates the average of `Aggregate rating`.

4. **Find Most Common Rating Color for Top-Rated Price Range**:
   - Identifies the price range with the highest average rating.
   - Filters the dataset to that price range and finds the most frequent `Rating color`.

---

## ✅ Output Example

