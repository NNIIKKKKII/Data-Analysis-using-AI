# 🛠️ Feature Engineering on Restaurant Dataset

This project focuses on enhancing the dataset by extracting additional features and encoding categorical values to make it more suitable for data analysis or machine learning models.

## 📂 Dataset

- File: `Dataset .csv`
- Source: Restaurant listing data (includes columns like Restaurant Name, Address, Table Booking, and Online Delivery)

---

## 🎯 Objectives

1. **Extract new features** from text-based columns.
2. **Encode categorical variables** into numerical formats for easier analysis and modeling.

---

## 🧪 Feature Engineering Steps

### ✅ Step 1: Length-Based Features
- `Restaurant Name Length`: Number of characters in each restaurant's name.
- `Address Length`: Number of characters in each restaurant's address.

### ✅ Step 2: Categorical Encoding
- `Has Table Booking Encoded`:  
  - `1` if table booking is available (`Yes`)  
  - `0` otherwise
- `Has Online Delivery Encoded`:  
  - `1` if online delivery is available (`Yes`)  
  - `0` otherwise

---

## 🧾 Sample Output

| Restaurant Name | Name Length | Address        | Address Length | Table Booking | Encoded | Online Delivery | Encoded |
|-----------------|-------------|----------------|----------------|----------------|---------|------------------|---------|
| ABC Restaurant  | 14          | 123 MG Road    | 11             | Yes            | 1       | No               | 0       |
| XYZ Diner       | 9           | 456 Park Ave   | 12             | No             | 0       | Yes              | 1       |

---

## 🛡️ Error Handling

- Missing values in `Restaurant Name` or `Address` are safely handled using `.fillna('')`.
- Case-insensitive comparison is used while encoding categorical values.

---

## 🧰 Requirements

- Python 3.x
- pandas

You can install the dependencies using:

```bash
pip install pandas
