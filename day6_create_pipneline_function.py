import duckdb

def run_duckdb_etl(input_csv: str, output_parquet: str):
    con = duckdb.connect()

    etl_query = f"""
    COPY (
        SELECT
            Name,
            Age,
            Email,
            JoinDate
        FROM read_csv_auto('{input_csv}')
        WHERE
            Name IS NOT NULL
            AND Age IS NOT NULL
            AND regexp_matches(Email, '^[^@]+@[^@]+\.[^@]+$')
    ) TO '{output_parquet}' (FORMAT 'parquet');
    """

    con.execute(etl_query)
    print(f"ETL completed: {output_parquet}")


if __name__ == "__main__":
    run_duckdb_etl('dirty_data.csv', 'cleaned_data_function.parquet')