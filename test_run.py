import sqlite3
from main import load_csv, run_query, get_table_name


def main():
    conn = sqlite3.connect(":memory:")
    path = "tests/sample.csv"
    load_csv(conn, path)
    table = get_table_name(path)
    print(f"\n查詢資料表: {table}\n")
    run_query(conn, f"SELECT * FROM {table};")


if __name__ == "__main__":
    main()
