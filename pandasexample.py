import pandas as pd

# Load your CSV file (replace with your actual file path if necessary)
df = pd.read_csv('data.csv')  # Use the file name or full path here

# Show the first 5 rows
print("First 5 rows of the dataset:")
print(df.head())

# Select specific columns
print("\nSelecting 'total_bill' and 'tip' columns:")
print(df[['total_bill', 'tip']].head())

# Handling missing values (if any)
print("\nChecking for missing values:")
print(df.isnull().sum())

# Drop rows with missing values (if any)
df_cleaned = df.dropna()
print("\nDataset after dropping rows with missing values:")
print(df_cleaned.head())

# Basic statistics of the dataset
print("\nBasic statistics of the dataset:")
print(df.describe())
