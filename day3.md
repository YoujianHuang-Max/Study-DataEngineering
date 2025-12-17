# Day 3 – File Formats

## 1. Learning Objectives
- Understand the basics of **CSV, JSON, and Parquet** file formats  
- Learn how to **read and write** these formats in Python  
- Understand **why Parquet is more suitable for big data**  

---

## 2. File Format Basics

| Format  | Description | Pros | Cons |
|---------|------------|------|------|
| CSV     | Comma-separated values, plain text | Simple, easy to read, widely compatible | Large file size, no type info, no compression |
| JSON    | JavaScript Object Notation, semi-structured | Supports nested data, readable | Slower to read, larger file size |
| Parquet | Columnar storage, binary format | Highly efficient for big data, supports compression, preserves data types | Not human-readable |

**Why Parquet is better for big data:**  
- Columnar storage → only read needed columns  
- Compressed storage → saves disk space  
- Preserves data types → avoids CSV type inference  

## 3. Summary

- **CSV**: easy, compatible, but large and slower for big data  
- **JSON**: semi-structured, supports nested data, larger file size  
- **Parquet**: columnar, compressed, preserves types, fast for large datasets  
- Can convert between formats: **CSV → Parquet → JSON**  
- For big data, **Parquet is preferred** for storage and query efficiency  

---

## 4. Practice Tips

- Try saving CSV to both Parquet and JSON, then read them back  
- Experiment with reading only a few columns to see performance differences  
- Compare file sizes of CSV, Parquet, and JSON for the same dataset  


