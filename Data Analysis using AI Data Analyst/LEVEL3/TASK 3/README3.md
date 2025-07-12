
# 🍽️ Restaurant Ratings Data Visualization Project

This project uses Python libraries like **Pandas**, **Matplotlib**, and **Seaborn** to analyze and visualize restaurant rating data. The goal is to gain insights by exploring distributions and relationships between features and the target variable – **Aggregate Rating**.

---

## 📊 Task Overview

### ✅ 1. Visualize Rating Distribution
- **Histogram** to show frequency distribution of ratings
- **Bar plot** to show count of each rating level

### ✅ 2. Compare Average Ratings
- **By Cuisine**: Extracted the first cuisine type to simplify grouping
- **By City**: Analyzed top 15 cities with highest average ratings

### ✅ 3. Analyze Feature Relationships
- Relationship between `Average Cost for Two` and `Aggregate Rating`
- Relationship between `Votes` and `Aggregate Rating`

---

## 🛠️ Requirements

Make sure the following Python libraries are installed:

```bash
pip install pandas matplotlib seaborn
```

---

## 📁 File Structure

```
project-folder/
│
├── Dataset.csv                # Your input dataset (Zomato or similar)
├── visualization.py           # The Python script with all visualizations
└── README.md                  # This file
```

---

## 🚀 How to Run

1. Place your dataset in the same directory as the script and rename it to `Dataset.csv`.
2. Run the script:

```bash
python visualization.py
```

---

## 📌 Notes

- The script assumes the dataset contains columns like:
  - `Aggregate rating`
  - `Cuisines`
  - `City`
  - `Average Cost for two`
  - `Votes`

- The `Cuisines` column may contain multiple cuisines per row (e.g., `Italian, Chinese`). Only the **first cuisine** is used for clarity in bar plots.

- Only the **top 15 cities and cuisines** are shown to keep the visuals readable.

---

## 📷 Sample Visualizations

- Distribution of ratings (histogram & bar plot)
- Average rating by top cuisines
- Average rating by city
- Scatter plots showing correlation between cost/votes and ratings

---

## 📞 Contact

For any questions or contributions, feel free to reach out.
