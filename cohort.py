# Important libraries
import pandas as pd

data = pd.read_csv("cohorts.csv")
print(data.head())

# Checking if there's any missing values or null values 
missing_values = data.isnull().sum()
print(missing_values)

# Data types of the different columns
data_types = data.dtypes
print(data_types)


# Convert 'Date' column to datetime format
data['Date'] = pd.to_datetime(data['Date'], format='%d/%m/%Y')

# Display the descriptive statistics of the dataset
descriptive_stats = data.describe()
print(descriptive_stats)
