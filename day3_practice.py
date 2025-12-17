# day3_file_formats_practice.py

import pandas as pd
import pyarrow  # Required for Parquet

# ---------------------------
# 1️⃣ Read CSV
# ---------------------------
csv_file = "Pre-2023 Apartment Building Evaluations.csv"
df_csv = pd.read_csv(csv_file)
print("CSV head:")
print(df_csv.head())

# ---------------------------
# 2️⃣ Save and Read Parquet
# ---------------------------
parquet_file = "Apartment Building Evaluations.parquet"
df_csv.to_parquet(parquet_file, engine='pyarrow', index=False)
df_parquet = pd.read_parquet(parquet_file, engine='pyarrow')
print("\nParquet head:")
print(df_parquet.head())

# ---------------------------
# 3️⃣ Save and Read JSON
# ---------------------------
json_file = "Pre-2023 Apartment Building Evaluations.json"
df_csv.to_json(json_file, orient='records', lines=True)
df_json = pd.read_json(json_file, orient='records', lines=True)
print("\nJSON head:")
print(df_json.head())

# ---------------------------
# 4️⃣ Read only selected columns
# ---------------------------
cols_to_read = ["YEAR_BUILT", "PROPERTY_TYPE"]

# CSV
df_csv_partial = pd.read_csv(csv_file, usecols=cols_to_read)
print("\nCSV Partial Columns:")
print(df_csv_partial.head())

# Parquet
df_parquet_partial = pd.read_parquet(parquet_file, columns=cols_to_read)
print("\nParquet Partial Columns:")
print(df_parquet_partial.head())

# Note: JSON does not natively support reading only specific columns