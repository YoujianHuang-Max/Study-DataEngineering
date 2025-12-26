## Week 2 – Local Data Lake, ETL & Architecture Concepts (Day 8–Day 12)

This week focuses on **core data engineering concepts** and **hands-on practice** using a **local simulation** of cloud services (S3, Glue, Lambda), followed by architectural understanding of data warehouses and data lakes.

---

## Day 8 – Cloud Foundations (Local Simulation)

### Goal
Understand foundational cloud concepts without using real cloud accounts.

### Key Concepts

- **Region**
  - A geographic location where cloud resources are hosted
  - Used to reduce latency and meet compliance requirements

- **IAM (Identity and Access Management)**
  - Controls who can access what
  - Includes users, roles, and permissions
  - In local simulation: replaced by folder-level access and scripts

- **S3 (Object Storage)**
  - Stores files (objects) inside buckets
  - Flat storage with logical folder prefixes
  - Highly scalable and durable in real cloud

### Local Simulation Strategy

Instead of AWS Console:
- Use local folders to simulate S3 buckets
- Use Python scripts to simulate upload / download behavior

---

## Day 9 – S3 Operations (Local Simulation)

### Goal
Simulate common S3 operations locally.

### Simulated Data Lake Structure
my_local_data_lake/
├── raw/
├── staging/
└── curated/
### Operations Practiced

- Upload file → copy local file into `raw/`
- Download file → copy file from `raw/` to working directory
- Move data to staging → copy from `raw/` to `staging/`

### Key Insight

This mirrors real S3 usage:
- Raw data is immutable
- Staging is used for transformation
- Curated is used for analytics-ready data

---

## Day 10 – AWS Glue Concepts (Local Understanding)

### Goal
Understand Glue without writing code.

### Glue Core Components

- **Crawler**
  - Scans data files
  - Infers schema (columns, data types)

- **Data Catalog**
  - Central metadata repository
  - Acts like a table definition layer

- **Job**
  - ETL logic
  - Reads data using catalog metadata
  - Writes transformed output

### Conceptual Flow
Data Files
↓
Crawler
↓
Catalog (Metadata)
↓
ETL Job
↓
Transformed Data

### Local Mapping

| AWS Glue | Local Equivalent |
|--------|------------------|
| Crawler | Inspecting CSV / Parquet with Pandas |
| Catalog | Knowing schema manually |
| Job | Python ETL script |

---

## Day 11 – Lambda (Local Simulation)

### Goal
Understand serverless file-based processing.

### What is Lambda?

- Event-driven function
- No server management
- Executes small tasks automatically

### Local Lambda Simulation

- A Python function that:
  - Triggers when a file appears
  - Reads input file
  - Transforms data
  - Writes a **new output file**

### Key Concept: Output Independence

- Output files are **new files**
- Original input files remain unchanged
- This ensures:
  - Data traceability
  - Reproducibility
  - Safe re-processing

### Example Flow
raw/orders.csv
↓
Lambda-like function
↓
curated/orders_cleaned.csv


## Day 12 – Data Warehouse vs Data Lake

### OLTP vs OLAP

| Feature | OLTP | OLAP |
|------|------|------|
| Purpose | Transactions | Analytics |
| Writes | Frequent | Rare |
| Reads | Simple | Complex |
| Schema | Normalized | Denormalized |
| Example | Order system | BI dashboard |

---

### Data Lake vs Data Warehouse

| Feature | Data Lake | Data Warehouse |
|------|----------|----------------|
| Data Types | Raw, any format | Structured |
| Storage | Files (S3) | Tables |
| Use Case | ML, exploration | Reporting |
| Flexibility | High | Medium |
| Performance | Depends | Optimized |

---

### Lakehouse Concept

Lakehouse = **Data Lake + Data Warehouse**

- Uses data lake storage
- Adds:
  - ACID transactions
  - SQL performance
  - Schema enforcement

Examples:
- Databricks + Delta Lake
- Snowflake + External Tables
- BigQuery + Cloud Storage

---

### Typical Layered Architecture
raw/
└── original data

staging/
└── cleaned & standardized data

curated/
└── analytics-ready datasets



