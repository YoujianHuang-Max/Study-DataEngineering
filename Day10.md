### Day 10: AWS Glue Basics (Local Simulation)

**Goal:** Understand AWS Glue concepts and how ETL jobs are structured. No cloud operation required, only conceptual understanding and local simulation.

---

#### 1. What is AWS Glue
- Fully managed ETL service on AWS
- Automatically discovers, cleans, transforms, and loads data
- Core components:
  - **Crawler**: Scans data sources (S3, RDS, etc.) to infer schema
  - **Catalog**: Stores metadata like table names, columns, types
  - **Job**: Defines ETL process using Python or Spark

---

#### 2. Glue Crawler
- Automatically scans data sources
- Detects columns, data types, partitions
- Updates the Glue Data Catalog
- **Local simulation:**  
  Use Python to read CSV files and inspect column names and types, simulating Crawler behavior

---

#### 3. Glue Job
- Defines ETL workflow:
  1. **Extract:** Read data from source (S3, database)
  2. **Transform:** Clean, validate, aggregate
  3. **Load:** Save to target (S3, Redshift, Snowflake)
- **Local simulation:**  
  Python reads CSV from `raw/`, transforms/cleans, writes to `staging/` or `curated/`

---

#### 4. Glue Data Catalog
- Stores metadata: table names, column types, partitions
- Acts like a schema repository
- **Local simulation:**  
  Use `pandas.DataFrame.dtypes` or CSV headers to represent table schema

---

#### 5. Summary
- Day 10 focuses on **concepts**, not actual cloud operations
- Key ideas to remember:
  - **Crawler** → Scan data to generate schema
  - **Catalog** → Store metadata
  - **Job** → Perform ETL workflow
- Local simulation helps understand Glue architecture and prepares for real ETL practice
<img width="1536" height="1024" alt="ChatGPT Image Dec 24, 2025, 03_21_54 PM" src="https://github.com/user-attachments/assets/abd90f78-cc4c-49ac-8a26-dcd2e912cb50" />
