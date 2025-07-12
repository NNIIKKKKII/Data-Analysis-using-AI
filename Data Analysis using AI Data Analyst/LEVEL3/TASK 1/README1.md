
# 🍽️ Restaurant Rating Prediction

## 📌 Objective
This project aims to build and evaluate regression models that predict the **Aggregate Rating** of a restaurant using its available features such as table booking availability, online delivery, price range, and more.

---

## 🛠️ Features Used
- Restaurant Name Length
- Address Length
- Has Table Booking (Encoded)
- Has Online Delivery (Encoded)
- Price Range (One-hot encoded)
- Rating Color (One-hot encoded)

---

## 🧪 Machine Learning Models
Three different models were trained and evaluated:
- 🔹 Linear Regression
- 🌳 Decision Tree Regressor
- 🌲 Random Forest Regressor

---

## 🧬 Dataset
The dataset used is `Dataset.csv`, which includes restaurant metadata such as:
- Name
- Address
- Locality
- Cuisines
- Has Table Booking
- Has Online Delivery
- Aggregate Rating
- Rating Color
- Price Range

---

## 🔍 Workflow

1. **Load and Clean Data**
2. **Feature Engineering**
   - One-hot encoding of categorical columns: `Has Table booking`, `Has Online delivery`, `Price range`, `Rating color`
   - Dropped irrelevant columns like `Restaurant Name`, `Address`, `Locality`, `Cuisines`, `Currency`, etc.
3. **Split Data**
   - 80% Training, 20% Testing using `train_test_split`
4. **Train Models**
   - Linear Regression
   - Decision Tree Regressor
   - Random Forest Regressor
5. **Evaluate Models**
   - Metrics: MAE, MSE, R²

---

## 📊 Evaluation Metrics

Each model is evaluated on:
- **MAE** (Mean Absolute Error)
- **MSE** (Mean Squared Error)
- **R² Score** (Coefficient of Determination)

```python
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
```

---

## 📈 Results Example

```text
--- Linear Regression ---
   MAE: 0.362
   MSE: 0.232
   R²: 0.58

--- Decision Tree ---
   MAE: 0.210
   MSE: 0.096
   R²: 0.81

--- Random Forest ---
   MAE: 0.175
   MSE: 0.072
   R²: 0.86
```

(Note: Actual results may vary depending on data and preprocessing.)

---

## 💡 Conclusion
The **Random Forest Regressor** performed the best based on MAE, MSE, and R² metrics, making it the most reliable model for predicting restaurant ratings in this context.

---

## 🧰 Tools & Libraries
- Python
- Pandas
- Scikit-learn
- NumPy

---

## 👨‍💻 Author
Nikhil Pareeshwad

---

## 📝 License
This project is open-source and free to use for educational purposes.
