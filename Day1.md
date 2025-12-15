# Day 1
# Data Engineering – Core Concepts

# 1. What is Data Engineering?
Data engineering focuses on building reliable, scalable data pipelines that move data from source systems into analytical platforms. 
The goal is to ensure data is available, clean, and trustworthy so analysts and data scientists can focus on insights rather than data collection.

# 2. ETL vs ELT

# ETL (Extract → Transform → Load)
- Data is transformed before loading into the data warehouse
- Traditional approach
- Transformation logic handled by data engineering pipelines
- Use cases: Smaller datasets; Fixed schemas; Limited warehouse compute

# ELT (Extract → Load → Transform)
- Raw data is loaded first, then transformed inside the warehouse
- Modern cloud-native approach
- Heavy use of SQL and warehouse compute
- Use cases: Large-scale data; Flexible analytics; Analysts involved in data modeling

# 3.Data Pipeline
  -A data pipeline is an automated process that moves data from source to destination in a repeatable and reliable way.
  -Typical flow: Source → Ingest → Transform → Store → Serve
  -Key characteristics: Automated; Monitored; Recoverable
  -Tools: Airflow; 

# 4.Batch vs Streaming Processing
  Batch Processing
  -Processes data in groups at scheduled intervals
  -High throughput, lower urgency
  -Examples: Daily sales reports, Nightly data warehouse refresh

  Streaming Processing
  -Processes data continuously in near real time
  -Low latency, high urgency
  -Examples: Fraud detection, Real-time alerts

# 5.Data Warehouse
  -A data warehouse is a centralized system optimized for analytical queries.
  -Characteristics: Structured data, SQL-based, Optimized for read-heavy workloads
  -Examples: Snowflake, BigQuery, Amazon Redshift

# 6.Data Lake & Lakehouse
  # Data Lake
    -Stores raw data in original format
    -Supports structured and unstructured data
    -Low storage cost
  # Lakehouse
    -Combines data lake storage with warehouse-style analytics
    -Supports both raw data and structured querying
    -Modern architecture trend

# 7.Big Picture View
  # Sources → Data Engineering → Data Warehouse/Lake → Analytics & BI
  -Data engineers focus on data movement, reliability, and scalability, enabling downstream analysis and decision-making.

# 8.Summary
  -Data engineering is about designing and maintaining data pipelines using concepts like ETL/ELT, batch and streaming processing, 
   and modern data storage systems such as data warehouses and lakehouses. It ensures data is accessible, reliable, and scalable for analytical use.
