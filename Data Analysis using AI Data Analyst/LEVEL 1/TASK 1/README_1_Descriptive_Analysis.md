# 📊 Descriptive Analysis of Restaurant Dataset

## ✅ Objective
Perform a comprehensive descriptive analysis on the restaurant dataset to:
- Understand dataset structure
- Handle missing data
- Convert relevant columns to categorical types
- Explore the distribution of the target variable `Aggregate rating`

---

## 📌 Key Steps in the Code

### 1. Load the Dataset
- File path: `LEVEL 1\Dataset .csv`
- Loaded using `pandas.read_csv()`
- Displayed shape and first 5 rows

### 2. Missing Value Handling
- Checked for missing values in all columns
- Filled missing values in the `'Cuisines'` column with `'Unknown'`
- Re-verified missing values after imputation

### 3. Data Type Inspection & Conversion
- Checked original data types of all columns
- Converted relevant columns to `category` type:
  - `Has Table booking`
  - `Has Online delivery`
  - `Is delivering now`
  - `Switch to order menu`

### 4. Target Variable Analysis: `Aggregate rating`
- Plotted histogram with KDE to visualize distribution
- Displayed summary statistics (mean, std, min, max, etc.)
- Plotted count plot to check for class imbalance
- Displayed percentage distribution of each rating class

---

## 📊 Output Summary
- Dataset shape and head preview
- Missing value report before and after handling
- Converted column types
- Histogram and countplot of `Aggregate rating`
- Descriptive statistics and class distribution

---

## 📂 Dataset Used
- Filename: `Dataset .csv`
- Location: Inside folder `LEVEL 1`

---

## 💾 Dependencies

Make sure the following Python libraries are installed:
```bash
pip install pandas matplotlib seaborn
