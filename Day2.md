# Day 2 – Data Storage Basics

## 1. Basics of S3 / Google Cloud Storage (GCS)

**What is S3 / GCS?**  
- Cloud-based object storage service  
- Can store large-scale data persistently  
- Object storage, not a traditional file system  
- Supports access control, versioning, and lifecycle management  

**Key Concepts**

| Concept | Description |
|---------|------------|
| Bucket  | Top-level directory in cloud storage, a container for objects |
| Object  | Data unit stored in a bucket, e.g., CSV files, images, JSON |

**Data Lake Layers**

| Layer    | Description |
|----------|-------------|
| raw      | Raw data, unprocessed |
| staging  | Temporary layer, basic cleaning/formatting |
| curated  | Final structured and analysis-ready data |

---

## 2. Simulating S3 Locally

**Example directory structure:**

**Sample CSV files**

**sales.csv (raw layer)**

```csv
date,product,sales
2025-12-16,apple,100
2025-12-16,banana,150
inventory_id,product_id,product_name,brand,quantity_on_hand,unit_cost,last_received_date
1,101,apple,BrandA,200,0.5,2025-12-01
2,102,banana,BrandB,300,0.3,2025-12-03

:: Copy files to staging
copy raw\sales.csv staging\sales.csv
copy raw\inventory.csv staging\inventory.csv

:: Copy files to curated
copy staging\sales.csv curated\sales.csv
copy staging\inventory.csv curated\inventory.csv

:: View directory structure
tree /F



