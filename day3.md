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

## 3. Practice Tips

- Try saving CSV to both Parquet and JSON, then read them back  
- Experiment with reading only a few columns to see performance differences  
- Compare file sizes of CSV, Parquet, and JSON for the same dataset  

## 4.Overview

| Feature | CSV | JSON | Parquet |
|---------|-----|------|---------|
| **Description** | Text file with comma‑separated values, rows separated by new lines | Open format for structured and semi‑structured data, widely used by APIs and NoSQL | Columnar, binary storage designed for big data with schema metadata |
| **Read Speed** | Quick for small files but slows on large datasets | Usually loads entire file into memory — slower for large files | Very fast, optimized for analytical queries |
| **File Size** | Compact and compresses well, larger than Parquet | Larger than CSV due to repeated keys | Smallest of the three, efficient storage |
| **Splittable** | Easy to split | Splittable but more complex | Easily splittable |
| **Included Data Types** | No explicit types; inferred when parsing | Defines strings, numbers, lists, objects; types inferred | Strong schema and enforced types |
| **Easy to Read** | Very easy for humans and tools | Easy if formatted; otherwise hard | Not human‑readable without tools |
| **Nestable** | Not supported | Excellent support for nested data | Supports nested and complex types |
| **Columnar / Row‑based** | Row‑based | Row‑based | Columnar |
| **Complex Data Structures** | Not supported | Supports objects and lists | Supports higher‑level types like timestamps, nested groups |

## Pros and Cons

**CSV**
- **Pros:** Universal support, human‑readable, compresses well :contentReference[oaicite:2]{index=2}  
- **Cons:** No built‑in types, slower on large files, no nesting or complex types :contentReference[oaicite:3]{index=3}

**JSON**
- **Pros:** Great for nested or unstructured data, readable when formatted :contentReference[oaicite:4]{index=4}  
- **Cons:** Often needs full file in memory, larger than CSV/Parquet :contentReference[oaicite:5]{index=5}

**Parquet**
- **Pros:** Fast read speed, small file size, schema‑aware, handles nested/complex data well :contentReference[oaicite:6]{index=6}  
- **Cons:** Hard to inspect without code/tools :contentReference[oaicite:7]{index=7}

## When to Use Each

- **CSV:** Good for small, tabular data where human inspection is important.  
- **JSON:** Best for semi‑structured or nested data, especially from APIs.  
- **Parquet:** Ideal for large‑scale analytics, data lakes, and performance‑critical workflows.

