# 📊 Restaurant Dataset: Descriptive & Categorical Analysis

## ✅ Objective
Perform descriptive analysis on numerical columns and explore the distribution of key categorical variables like:
- `Country Code`
- `City`
- `Cuisines`

---

## 📌 Project Overview

This script helps in understanding the restaurant dataset by:
- Calculating statistical summaries for numerical columns
- Identifying top contributing values in major categorical columns
- Preparing data for potential visualization or further analysis

---

## 🔍 Features of the Code

### 1. **Load Dataset**
- File loaded using: `pd.read_csv("LEVEL 1\\Dataset .csv")`
- Data is expected to contain information such as ratings, city, cuisines, and location

### 2. **Numerical Column Analysis**
- Uses `DataFrame.describe()` to calculate:
  - Mean
  - Standard deviation
  - Minimum and maximum values
  - Quartiles (25%, 50%, 75%)
- Helps in summarizing key metrics at a glance

### 3. **Categorical Distribution**
- **Top 10 Country Codes** with the most restaurants
- **Top 10 Cities** with the highest number of listings
- **Top 10 Cuisines** by frequency
  - Handles multiple cuisines per entry by splitting and flattening the list
  - Strips spaces for accurate grouping

---

## 📊 Sample Output

Example outputs you can expect:
