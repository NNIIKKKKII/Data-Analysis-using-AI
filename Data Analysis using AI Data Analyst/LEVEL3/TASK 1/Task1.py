import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Load dataset
file_path = "Data Analysis using AI Data Analyst\LEVEL 3\TASK 1\Dataset.csv" # Corrected filename (removed extra space)
data = pd.read_csv(file_path)


# Drop rows with missing target
data = data.dropna(subset=['Aggregate rating'])

# Drop unnecessary columns
columns_to_drop = ['Restaurant Name', 'Address', 'Locality', 'Locality Verbose', 'Cuisines', 'Currency', 'Rating text']
data = data.drop(columns=columns_to_drop, errors='ignore')

# One-hot encode all remaining categorical columns
data_encoded = pd.get_dummies(data, drop_first=True)

# Define features and target
features = data_encoded.drop(columns=['Aggregate rating'], errors='ignore')
target = data_encoded['Aggregate rating']

# Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Models
models = {
    'Linear Regression': LinearRegression(),
    'Decision Tree': DecisionTreeRegressor(random_state=42),
    'Random Forest': RandomForestRegressor(random_state=42)
}

# Train & Evaluate
results = {}
for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    
    results[name] = {
        'MAE': round(mean_absolute_error(y_test, y_pred), 4),
        'MSE': round(mean_squared_error(y_test, y_pred), 4),
        'R²': round(r2_score(y_test, y_pred), 4)
    }

# Display results
# Display results
print("\nModel Performance:")
for model, scores in results.items():
    print(f"\n--- {model} ---")
    for metric, val in scores.items():
        print(f"   {metric}: {val}")
