# Week 2 – Local S3 / Data Lake Simulation

## Day 8: AWS Basics (Local Simulation)

**Goal:** Understand key AWS concepts without touching the real console.

- **Region:** Geographical location of data centers  
- **IAM:** Identity and Access Management, user and permission control  
- **S3:** Simple Storage Service, stores objects in buckets  

**Local Simulation Notes:**

- Instead of AWS, we simulate a **local data lake** on disk:
- Each folder represents a layer in the data lake:
- `raw/` – original data
- `staging/` – intermediate processing
- `curated/` – final clean dataset
- Operations like upload/download are done via Python `shutil` or terminal copy commands.

---
