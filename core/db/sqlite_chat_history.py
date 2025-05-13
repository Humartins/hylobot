import sqlite3
from langchain_core.messages import AIMessage, HumanMessage, BaseMessage
from langchain_core.chat_history import BaseChatMessageHistory
from pathlib import Path
from typing import List

DB_PATH = Path(__file__).resolve().parent / "hylo_chat.db"

class SQLiteChatMessageHistory(BaseChatMessageHistory):
    def __init__(self, session_id: str):
        self.session_id = session_id
        self._create_table()

    def _create_table(self):
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS chat_messages (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    session_id TEXT,
                    role TEXT,
                    content TEXT,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            """)
            conn.commit()

    @property
    def messages(self) -> List[BaseMessage]:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT role, content FROM chat_messages
                WHERE session_id = ?
                ORDER BY timestamp ASC
            """, (self.session_id,))
            rows = cursor.fetchall()

        messages = []
        for role, content in rows:
            if role == "user":
                messages.append(HumanMessage(content=content))
            elif role == "assistant":
                messages.append(AIMessage(content=content))
        return messages

    def add_message(self, message: BaseMessage) -> None:
        role = "assistant" if isinstance(message, AIMessage) else "user"
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO chat_messages (session_id, role, content)
                VALUES (?, ?, ?)
            """, (self.session_id, role, message.content))
            conn.commit()

    def clear(self) -> None:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                DELETE FROM chat_messages WHERE session_id = ?
            """, (self.session_id,))
            conn.commit()
