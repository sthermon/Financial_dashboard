import sqlite3
from pathlib import Path

'''Example'''

DB_PATH = Path(__file__).resolve().parent.parent / "db" / "financial_data.db"

def connect_db():
    return sqlite3.connect(DB_PATH)