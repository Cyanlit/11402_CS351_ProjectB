import sqlite3
import os
import pytest
from main import load_csv, run_query, get_table_name


SAMPLE_CSV = os.path.join(os.path.dirname(__file__), "sample.csv")


def test_get_table_name_simple():
    assert get_table_name("tests/sample.csv") == "sample"


def test_get_table_name_nested():
    assert get_table_name("/some/path/my_data.csv") == "my_data"


def test_load_csv_row_count():
    conn = sqlite3.connect(":memory:")
    load_csv(conn, SAMPLE_CSV)
    cur = conn.execute("SELECT COUNT(*) FROM sample")
    assert cur.fetchone()[0] == 3


def test_load_csv_columns():
    conn = sqlite3.connect(":memory:")
    load_csv(conn, SAMPLE_CSV)
    cur = conn.execute("SELECT id, name, age FROM sample WHERE id=1")
    row = cur.fetchone()
    assert row == (1, "Alice", 30)


def test_load_csv_missing_file(capsys):
    conn = sqlite3.connect(":memory:")
    load_csv(conn, "nonexistent.csv")
    captured = capsys.readouterr()
    assert "檔案不存在" in captured.out


def test_run_query_select(capsys):
    conn = sqlite3.connect(":memory:")
    load_csv(conn, SAMPLE_CSV)
    run_query(conn, "SELECT * FROM sample")
    captured = capsys.readouterr()
    assert "Alice" in captured.out


def test_run_query_insert():
    conn = sqlite3.connect(":memory:")
    load_csv(conn, SAMPLE_CSV)
    run_query(conn, "INSERT INTO sample (id, name, age) VALUES (4, 'Dave', 28)")
    cur = conn.execute("SELECT COUNT(*) FROM sample")
    assert cur.fetchone()[0] == 4


def test_run_query_invalid_sql(capsys):
    conn = sqlite3.connect(":memory:")
    run_query(conn, "SELECT * FROM nonexistent_table")
    captured = capsys.readouterr()
    assert "查詢錯誤" in captured.out
