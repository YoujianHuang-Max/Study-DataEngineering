import pandas as pd

### Extract ###

# import data
df = pd.read_csv("dirty_data.csv")

# review data
print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())


### Transform ###

# drop rows with missing values in 'Name' or 'Email' columns
df_clean = df.dropna(subset=["Name", "Email"])

# fill missing values in 'Age' column with the mean age
df_clean["Age"] = df_clean["Age"].fillna(df_clean["Age"].mean())

# convert 'JoinDate' column to datetime format
df_clean["JoinDate"] = pd.to_datetime(df_clean["JoinDate"], errors='coerce')

# remove rows with invalid email addresses (simple check for '@' symbol)
df_clean = df_clean[df_clean["Email"].str.contains("@")]

# further clean email addresses using regex to ensure valid format
df_clean = df_clean[df_clean["Email"].str.match(r"[^@]+@[^@]+\.[^@]+")]

print("\nCleaned Data:")
print(df_clean)


### Load ###

# save cleaned data to a new CSV file
df_clean.to_csv("clean_data.csv", index=False)

# save cleaned data to a Parquet file
df_clean.to_parquet("clean_data.parquet", engine='pyarrow', index=False)