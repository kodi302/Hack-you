import sqlite3
from pathlib import Path

DB_DIR = Path("database")
DB_DIR.mkdir(exist_ok=True)

DB_FILE = DB_DIR / "hackyou.db"


class Database:

    def __init__(self):
        self.conn = sqlite3.connect(DB_FILE)
        self.cursor = self.conn.cursor()
        self.initialize()

    def initialize(self):

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS scan_history(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            module TEXT,
            target TEXT,
            result TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS settings(
            id INTEGER PRIMARY KEY,
            name TEXT,
            value TEXT
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS reports(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)

        self.conn.commit()

    def add_scan(self, module, target, result):

        self.cursor.execute(
            """
            INSERT INTO scan_history(module,target,result)
            VALUES(?,?,?)
            """,
            (module, target, result)
        )

        self.conn.commit()

    def scans(self):

        self.cursor.execute(
            "SELECT * FROM scan_history ORDER BY id DESC"
        )

        return self.cursor.fetchall()

    def save_setting(self, name, value):

        self.cursor.execute(
            """
            INSERT OR REPLACE INTO settings(id,name,value)
            VALUES(
                (SELECT id FROM settings WHERE name=?),
                ?,?
            )
            """,
            (name, name, value)
        )

        self.conn.commit()

    def get_setting(self, name):

        self.cursor.execute(
            "SELECT value FROM settings WHERE name=?",
            (name,)
        )

        row = self.cursor.fetchone()

        if row:
            return row[0]

        return None

    def add_report(self, filename):

        self.cursor.execute(
            """
            INSERT INTO reports(filename)
            VALUES(?)
            """,
            (filename,)
        )

        self.conn.commit()

    def reports(self):

        self.cursor.execute(
            "SELECT * FROM reports ORDER BY id DESC"
        )

        return self.cursor.fetchall()


db = Database()