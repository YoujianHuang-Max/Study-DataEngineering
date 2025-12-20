import pandas as pd
import time
import duckdb

# pandas ETL process
start = time.time()

df = pd.read_csv("dirty_data.csv")
df = df.dropna(subset=["Name", "Age"])
df = df[df["Email"].str.contains("@", na=False)]

result = df.groupby("JoinDate").size()

end = time.time()
print("\nPandas result:")
print(result)
print("Pandas time:", end - start)


# DuckDB ETL process
start = time.time()
con = duckdb.connect()
duckdb_result = con.execute("""
SELECT
    JoinDate,
    COUNT(*) AS cnt
FROM read_csv_auto('dirty_data.csv')
WHERE Name IS NOT NULL AND Age IS NOT NULL
GROUP BY JoinDate
""").fetchdf()

end = time.time()

print("\nDuckDB result:")
print(duckdb_result)
print("DuckDB time:", end - start)