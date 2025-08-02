import sqlite3
import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../data'))
MATERIAL_DB_PATH = os.path.join(BASE_DIR, 'materials.db')
PARTS_DB_PATH = os.path.join(BASE_DIR, 'parts.db')

def get_materials():
    conn = sqlite3.connect(MATERIAL_DB_PATH)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS materials (name TEXT UNIQUE, price REAL)")
    cursor.execute("SELECT name, price FROM materials")
    results = cursor.fetchall()
    conn.close()
    return results

def get_parts():
    conn = sqlite3.connect(PARTS_DB_PATH)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS parts (name TEXT UNIQUE, price REAL)")
    cursor.execute("SELECT name, price FROM parts")
    results = cursor.fetchall()
    conn.close()
    return results

def save_material_if_new(name, price):
    conn = sqlite3.connect(MATERIAL_DB_PATH)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS materials (name TEXT UNIQUE, price REAL)")
    try:
        cursor.execute("INSERT INTO materials (name, price) VALUES (?, ?)", (name, price))
        conn.commit()
    except sqlite3.IntegrityError:
        pass  # already exists
    conn.close()

def save_part_if_new(name, price):
    conn = sqlite3.connect(PARTS_DB_PATH)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS parts (name TEXT UNIQUE, price REAL)")
    try:
        cursor.execute("INSERT INTO parts (name, price) VALUES (?, ?)", (name, price))
        conn.commit()
    except sqlite3.IntegrityError:
        pass
    conn.close()
