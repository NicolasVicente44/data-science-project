import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load the dataset
file_path = r'C:\Users\starc\OneDrive\Desktop\LAKEHEAD SEMESTER 1\COMP-4112-FAO - Introduction to Data Science\Final Project\car_prices.csv'
data = pd.read_csv(file_path)

# Check for missing values
print("Missing values before cleaning:")
print(data.isnull().sum())

# Drop any rows with missing values
data.dropna(inplace=True)

# Check for missing values again
print("Missing values after cleaning:")
print(data.isnull().sum())

# Optimize data types
data['make'] = data['make'].astype('category')
data['model'] = data['model'].astype('category')
data['trim'] = data['trim'].astype('category')
data['condition'] = data['condition'].astype('float32')
data['year'] = data['year'].astype('int32')
data['odometer'] = data['odometer'].astype('float32')
data['mmr'] = data['mmr'].astype('float32')
data['sellingprice'] = data['sellingprice'].astype('float32')

# Select features and target variable
X = data[['year', 'make', 'condition', 'odometer']]  # Adjust as needed
y = data['sellingprice']

# One-hot encode categorical variables
X = pd.get_dummies(X, drop_first=True)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'Mean Squared Error: {mse}')
print(f'R^2 Score: {r2}')
