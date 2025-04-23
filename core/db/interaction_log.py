from datetime import datetime
from core.db.database import get_connection
import sqlite3

def salvar_interacao(user_input, bot_response, source=""):
    timestamp = datetime.now().isoformat(sep=' ', timespec='seconds')

    print(f"Salvando interação - Timestamp: {timestamp}, User input: {user_input}, Bot response: {bot_response}, Source: {source}")

    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO interactions (timestamp, user_input, bot_response, source)
                VALUES (?, ?, ?, ?)
            """, (timestamp, user_input, bot_response, source))
            conn.commit()
    except sqlite3.Error as e:
        print(f"Erro ao salvar interação: {e}")
