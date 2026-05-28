import sqlite3
import pandas as pd
import os
import sys
from tabulate import tabulate


def get_table_name(path: str) -> str:
    return os.path.splitext(os.path.basename(path))[0]


def load_csv(conn: sqlite3.Connection, path: str) -> None:
    if not os.path.exists(path):
        print(f"檔案不存在: {path}")
        return
    try:
        df = pd.read_csv(path)
    except Exception as e:
        print(f"讀取 CSV 發生錯誤: {e}")
        return
    table = get_table_name(path)
    try:
        df.to_sql(table, conn, if_exists="replace", index=False)
        print(f"已載入 {len(df)} 筆資料到資料表 '{table}'")
    except Exception as e:
        print(f"寫入資料庫發生錯誤: {e}")


def run_query(conn: sqlite3.Connection, sql: str) -> None:
    try:
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        cols = [d[0] for d in cur.description] if cur.description else []
        if cols:
            print(tabulate(rows, headers=cols, tablefmt="grid"))
        else:
            print("查詢已執行。")
    except Exception as e:
        print(f"查詢錯誤: {e}")


def repl():
    conn = sqlite3.connect(":memory:")
    print("CSV Mini DB REPL — 輸入 'help' 查看可用指令。")
    while True:
        try:
            line = input("> ")
        except (EOFError, KeyboardInterrupt):
            print("\n離開")
            break
        if not line:
            continue
        parts = line.strip().split(maxsplit=1)
        cmd = parts[0].lower()
        arg = parts[1] if len(parts) > 1 else ""

        if cmd in ("exit", "quit"):
            break
        if cmd == "help":
            print("可用指令:\n - load <filename>    載入 CSV 檔案為資料表\n - query <SQL>        執行 SQL 查詢 (對已載入的資料表)\n - tables             列出已載入的資料表\n - exit/quit          結束程式")
            continue
        if cmd == "load":
            if not arg:
                print("用法: load <filename>")
                continue
            load_csv(conn, arg)
            continue
        if cmd == "query":
            if not arg:
                print("用法: query <SQL>")
                continue
            run_query(conn, arg)
            continue
        if cmd == "tables":
            run_query(conn, "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;")
            continue

        print("未知指令，輸入 'help' 查看說明。")


if __name__ == "__main__":
    repl()
