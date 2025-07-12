# 📊 Table Booking and Online Delivery Analysis

This project performs a data analysis on a restaurant dataset to understand the trends in table booking, online delivery, ratings, and price ranges. It uses Python and pandas to uncover key insights through data grouping and aggregation.

---

## 📁 Dataset

The dataset contains information about restaurants, including:

- Restaurant name
- City and country
- Latitude and longitude
- Aggregate rating
- Table booking availability
- Online delivery availability
- Price range
- Cuisines and more

📌 **Filename:** `Dataset.csv`

> ⚠️ Ensure the file is correctly named and located in the same folder as the script.

---

## ✅ Objectives

1. Calculate the **percentage** of restaurants that offer:
   - Table booking
   - Online delivery

2. Compare **average ratings** of:
   - Restaurants with table booking
   - Restaurants without table booking

3. Analyze the **availability of online delivery** among different **price ranges**.

---

## 🧰 Tools Used

- Python
- pandas

---

## 🛠️ How It Works

### 1. Percentage Calculation

```python
data['Has Table booking'].value_counts(normalize=True) * 100
data['Has Online delivery'].value_counts(normalize=True) * 100
