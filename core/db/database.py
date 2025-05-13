import sqlite3
from pathlib import Path
from core.db.interaction_log import init_db

DB_PATH = Path(__file__).resolve().parent.parent.parent / "hylobot.db"

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    return conn

def initialize_database():
    init_db()
