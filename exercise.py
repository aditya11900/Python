# Exercise 1: From the given dataset print the first and last 7 rows of your dataframe.
# Check how many rows and columns are there.
# Display all column names and row names.
# Assign row indexes to your dataframe as "Row1, Row2, ...".
# Display the summary of each column of your dataframe.

import pandas as pd
import numpy as np

df = pd.read_csv("C:\\Users\\hp\\Downloads\\Automobile_data.csv")
print(df.head(7))
print(df.tail(7))
num_rows = df.shape[0]
num_cols = df.shape[1]

print("Number of rows: ", num_rows)
print("Number of columns: ", num_cols)

print("Column names: ", df.columns)
print("Row names: ", df.index)

print("indexing rows")
print(df.index.tolist())


print("Summary of each column")
print(df.describe())









