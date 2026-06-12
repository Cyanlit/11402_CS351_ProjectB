import sqlite3
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from main import load_csv, run_query, get_table_name


def main():
    conn = sqlite3.connect(":memory:")
    # 使用相對於項目根目錄的路徑
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    path = os.path.join(base_dir, "tests", "sample.csv")
    load_csv(conn, path)
    table = get_table_name(path)
    print(f"\n查詢資料表: {table}\n")
    run_query(conn, f"SELECT * FROM {table};")


if __name__ == "__main__":
    main()
