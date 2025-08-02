import sqlite3
import os

DB_PATH = os.path.join("data", "materials.db")

def init_db():
    os.makedirs("data", exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Tabelle erzeugen
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS materials (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            unit_price REAL NOT NULL,
            unit TEXT NOT NULL
        )
    ''')

    # Beispieldaten einfügen (nur wenn leer)
    cursor.execute("SELECT COUNT(*) FROM materials")
    if cursor.fetchone()[0] == 0:
        materials = [
            ("Schraube M4", 0.05, "Stück"),
            ("Drahtbindung", 0.20, "Stück"),
            ("Umschlag", 0.10, "Stück")
        ]
        cursor.executemany("INSERT INTO materials (name, unit_price, unit) VALUES (?, ?, ?)", materials)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
