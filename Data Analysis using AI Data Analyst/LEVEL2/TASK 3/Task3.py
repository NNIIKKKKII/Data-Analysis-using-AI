import pandas as pd

# Load the CSV file (make sure the file path is correct)
file_path = "Data Analysis using AI Data Analyst\LEVEL 2\TASK 3\Dataset .csv" # Corrected filename (removed extra space)
data = pd.read_csv(file_path)

# Handle missing values in 'Restaurant Name' and 'Address' columns
data['Restaurant Name'] = data['Restaurant Name'].fillna('')
data['Address'] = data['Address'].fillna('')

# 1️⃣ Extract additional features from existing columns
data['Restaurant Name Length'] = data['Restaurant Name'].apply(len)
data['Address Length'] = data['Address'].apply(len)

# 2️⃣ Encode categorical variables
data['Has Table Booking Encoded'] = data['Has Table booking'].apply(lambda x: 1 if str(x).strip().lower() == 'yes' else 0)
data['Has Online Delivery Encoded'] = data['Has Online delivery'].apply(lambda x: 1 if str(x).strip().lower() == 'yes' else 0)

# 3️⃣ Display the new features
print("\n First 5 rows with newly engineered features:\n")
print(data[[
    'Restaurant Name', 'Restaurant Name Length',
    'Address', 'Address Length',
    'Has Table booking', 'Has Table Booking Encoded',
    'Has Online delivery', 'Has Online Delivery Encoded'
]].head())
