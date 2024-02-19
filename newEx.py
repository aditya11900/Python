
# Exercise 2: Clean the dataset by handling missing values (Nans) and update the CSV file.
# 	a) By deleting the rows which contain any missing values
# 	b) By replacinng the missing values by a fixed constant

import pandas as pd
import numpy as np

df = pd.read_csv("C:\\Users\\hp\\Downloads\\Automobile_data.csv")

print("Before cleaning")
print(df)

print("After cleaning")
df = df.dropna()
print(df)

print("After replacing missing values with fixed constant")
df = pd.read_csv("C:\\Users\\hp\\Downloads\\Automobile_data.csv")
df = df.fillna(0)
print(df)

