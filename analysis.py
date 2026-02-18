import pandas as pd

# Load logon data
logon = pd.read_csv("dataset/logon.csv")

print("Logon Data Shape:", logon.shape)
print("\nColumns:")
print(logon.columns)

print("\nFirst 5 rows:")
print(logon.head())

print("\n---------------- FILE DATA ----------------\n")

file_data = pd.read_csv("dataset/file.csv")

print("File Data Shape:", file_data.shape)
print("\nColumns:")
print(file_data.columns)

print("\nFirst 5 rows:")
print(file_data.head())