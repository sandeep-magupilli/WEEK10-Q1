# Import pandas library
import pandas as pd

# Load CSV file into DataFrame
# Replace 'data.csv' with your actual file name
df = pd.read_csv('data.csv')

# Display first 5 rows
print("First 5 rows of the DataFrame:")
print(df.head())

# Display last 5 rows
print("\nLast 5 rows of the DataFrame:")
print(df.tail())

# Display information about the DataFrame
print("\nDataFrame Info:")
print(df.info())

# Display statistical summary of numerical columns
print("\nStatistical Summary:")
print(df.describe())
