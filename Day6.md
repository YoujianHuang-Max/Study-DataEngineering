### Day 6 DuckDB + Python Practice
Today focused on combining Python and DuckDB to build a simple but realistic ETL pipeline, while comparing it with a Pandas-based approach.
### 1. Goal of Day 6
- Combine SQL + Python in one workflow
- Build a simple ETL pipeline
- Add data validation
- Perform aggregation
- Compare Pandas vs DuckDB performance

### 2. ETL Pipeline Structure
- Extract: Read CSV data
- Transform: Clean and validate data
- Load: Save results to CSV / Parquet

### 3. Data Validation
   - Dropped rows with missing Name or Email
   - Filled missing Age values using the mean
   - Converted JoinDate to datetime with error handling
   - Validated email format using:

### 4. Aggregation Practice
- Pandas: groupby("JoinDate").count()
- DuckDB: SQL GROUP BY JoinDate

### 5. Pandas vs DuckDB Performance Comparison
- Results from the experiment:
  - Pandas was faster for this task
  - DuckDB showed slightly higher execution time
- Reason
  - The dataset was very small
  - DuckDB has extra overhead (engine initialization, SQL parsing, query planning)

### 6. Key Takeaways
- Pandas is ideal for quick analysis on small datasets
- DuckDB is powerful for analytical SQL and large data
- Combining Python and SQL provides flexibility
- ETL pipelines should include validation, transformation, and clear outputs
- Tool choice depends on data size and use case
