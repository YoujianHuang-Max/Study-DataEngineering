import duckdb

# Create in-memory DuckDB connection
con = duckdb.connect()

# Preview first 5 rows
preview_query = """
SELECT *
FROM read_csv_auto('dirty_data.csv')
LIMIT 5
"""

print("CSV Preview:")
print(con.execute(preview_query).fetchdf())

# Transform data
transform_query = """
SELECT
    Name,
    Age,
    Email,
    JoinDate
FROM read_csv_auto('dirty_data.csv')
WHERE
    Name IS NOT NULL
    AND Age IS NOT NULL
"""
cleaned_df = con.execute(transform_query).fetchdf()
print("\nCleaned Data:")
print(cleaned_df)

email_validation_query = """
SELECT
    Name,
    Age,
    Email,
    JoinDate
FROM read_csv_auto('dirty_data.csv')
WHERE
    Email IS NOT NULL
    AND regexp_matches(Email, '^[^@]+@[^@]+\.[^@]+$')
"""

# Check email validity
validated_df = con.execute(email_validation_query).fetchdf()

print("Validated Email Data:")
print(validated_df)

join_date_agg_query = """
SELECT
    JoinDate,
    COUNT(*) AS user_count
FROM read_csv_auto('dirty_data.csv')
WHERE
    JoinDate IS NOT NULL
GROUP BY JoinDate
ORDER BY JoinDate
"""

# Analyze JoinDate distribution
join_date_stats = con.execute(join_date_agg_query).fetchdf()

print("\nUser count per JoinDate:")
print(join_date_stats)

# Calculate aggregated results
agg_query = """
SELECT
    COUNT(*) AS total_rows,
    AVG(Age) AS avg_age
FROM read_csv_auto('dirty_data.csv')
WHERE Age IS NOT NULL
"""

agg_result = con.execute(agg_query).fetchdf()
print("\nAggregated Result:")
print(agg_result)

# Load cleaned data to Parquet
load_query = """
COPY (
    SELECT *
    FROM read_csv_auto('dirty_data.csv')
    WHERE Name IS NOT NULL AND Age IS NOT NULL
) TO 'cleaned_data_duckdb.parquet' (FORMAT 'parquet')
"""

con.execute(load_query)
print("\nETL pipeline finished! Parquet file saved as 'cleaned_data_duckdb.parquet'")
