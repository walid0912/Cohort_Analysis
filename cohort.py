# Important libraries
import pandas as pd

data = pd.read_csv("cohorts.csv")
print(data.head())

# Checking if there's any missing values or null values 
missing_values = data.isnull().sum()
print(missing_values)
