"""
Day 5 - DuckDB ETL Template
CSV -> SQL -> Parquet
"""

import duckdb

# ---------------------------------
# 1. Create DuckDB connection
# ---------------------------------
con = duckdb.connect()

# ---------------------------------
# 2. Inspect raw CSV data
# ---------------------------------
inspect_query = """
SELECT *
FROM read_csv_auto('dirty_data.csv')
LIMIT 5
"""

print("Preview CSV data:")
print(con.execute(inspect_query).fetchdf())

# ---------------------------------
# 3. Transform data using SQL
# ---------------------------------
transform_query = """
SELECT
    Name,
    Age
FROM read_csv_auto('dirty_data.csv')
WHERE
    Name IS NOT NULL
    AND Age IS NOT NULL
"""

print("\nTransformed data:")
print(con.execute(transform_query).fetchdf())

# ---------------------------------
# 4. Load result to Parquet
# ---------------------------------
load_query = """
COPY (
    SELECT
        Name,
        Age
    FROM read_csv_auto('dirty_data.csv')
    WHERE
        Name IS NOT NULL
        AND Age IS NOT NULL
) TO 'cleaned_data.parquet' (FORMAT 'parquet');
"""

con.execute(load_query)

print("\nETL completed successfully.")
print("Output file: cleaned_data.parquet")