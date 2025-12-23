## Day 9: S3 Operations (Local Simulation)

**Goal:** Practice basic S3 operations using local folders.

### Steps:

1. **Create bucket and folder structure**
  - `raw/`, `staging/`, `curated/` under `my_local_data_lake/`

2. **Upload files (simulate S3 upload)**
  - Copy CSV files from working directory into `raw/`
  - In Python:
    ```python
    shutil.copy("orders.csv", "my_local_data_lake/raw/orders.csv")
    ```

3. **Download files (simulate S3 download)**
  - Copy files from `raw/` to local working directory
  - Example:
    ```python
    shutil.copy("my_local_data_lake/raw/orders.csv", "orders_downloaded.csv")
    ```

4. **Move/Copy to staging (simulate ETL staging layer)**
  - Example:
    ```python
    shutil.copy("my_local_data_lake/raw/orders.csv", "my_local_data_lake/staging/orders_staging.csv")
    ```

5. **Verify file structure**
  - Check folder contents to ensure files are in correct layers
  - Example Python snippet:
    ```python
    for layer in ["raw", "staging", "curated"]:
        path = os.path.join("my_local_data_lake", layer)
        print(f"{layer}/: {os.listdir(path)}")
    ```

### Key Takeaways

- Local folders can **simulate S3 buckets** safely without AWS costs
- File operations (`copy`, `move`) help understand the **data flow** in a data lake
- `raw → staging → curated` is a standard pattern in data engineering pipelines
- Day 9 focuses on **file management and structure**, not data cleaning or transformation
