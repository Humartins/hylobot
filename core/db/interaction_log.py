import sqlite3
from datetime import datetime
from pathlib import Path

# Caminho do banco de dados
DB_PATH = Path(__file__).resolve().parent / "interacoes.db"

# Inicializa o banco de dados
def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT NOT NULL,
            role TEXT NOT NULL,
            content TEXT NOT NULL,
            timestamp TEXT NOT NULL
            )
        """)
        conn.commit()

# Salva uma nova interação
def salvar_interacao(user_id, role, content, timestamp=None):
    if timestamp is None:
        timestamp = datetime.now().isoformat()

    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO messages (user_id, role, content, timestamp)
            VALUES (?, ?, ?, ?)
        """, (user_id, role, content, timestamp))
        conn.commit()

# Carrega o histórico de conversas de um usuário específico
def load_conversation(user_id):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT role, content, timestamp FROM messages 
            WHERE user_id = ?
            ORDER BY timestamp ASC
        """, (user_id,))
        return cursor.fetchall()
