
# 🍽️ Zomato Restaurant Ratings Data Visualization

This project focuses on visualizing various aspects of a restaurant ratings dataset from Zomato. The goal is to analyze the distribution of ratings, compare ratings across cities and cuisines, and uncover relationships between features and the target variable (`Aggregate rating`).

---

## 📁 Dataset

- File: `Dataset.csv`
- Key Columns used:
  - `Aggregate rating`
  - `Cuisines`
  - `City`
  - `Has Table booking`
  - `Has Online delivery`
  - `Price range`
  - `Rating color`

---

## 📊 Visualizations

### 1. **Distribution of Ratings**
- **Histogram**: Shows how aggregate ratings are distributed across all entries.
- **Bar Plot**: Displays the count of each unique rating value.

### 2. **Average Rating by Cuisine**
- Extracts the **primary cuisine** (first in the list).
- Filters top 15 cuisines by frequency.
- Bar plot shows how different cuisines perform on average in terms of customer ratings.

### 3. **Average Rating by City**
- Filters top 15 cities by number of entries.
- Visualizes how customer satisfaction varies across cities.

### 4. **Correlation Heatmap**
- Encodes categorical variables (like online delivery, table booking, etc.)
- Displays the correlation of each feature with the aggregate rating.

---

## 🧪 Dependencies

Make sure the following Python packages are installed:

```bash
pip install pandas matplotlib seaborn
```

---

## ▶️ How to Run

1. Place the `Dataset.csv` file in your working directory.
2. Run the Python script provided (`Task1.py` or similar).
3. The plots will be displayed sequentially for analysis.

---

## 📌 Insights Expected

- Which cuisines and cities have higher-rated restaurants?
- Are online delivery or table booking options related to better ratings?
- Do pricing levels affect customer satisfaction?

---

## 📷 Sample Output (Expected Plots)

- Distribution of ratings (histogram + bar)
- Top cuisines by average rating
- Top cities by average rating
- Correlation heatmap of all features with ratings

---

## ✍️ Author

- **Nikhil Pareeshwad**
- Project: Zomato Ratings Analysis for Data Science Level 3
- Guided by: Aishwarya B

---

## 📂 Project Structure

```
📁 LEVEL3
 ┣ 📄 Task1.py
 ┣ 📄 Dataset.csv
 ┗ 📄 README.md
```

---

## ✅ Status

✔️ Completed basic data visualizations  
✔️ Ready for deeper insights or ML modeling
