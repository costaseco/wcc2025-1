import sqlite3

list = ['Eggs', 'Milk', 'Bread', 'Butter']

def init_db():
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute("""
CREATE TABLE IF NOT EXISTS items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
)
""")

    items_exist = conn.execute("SELECT * FROM items").fetchone()
    if not items_exist:
        for item in list:
            cursor.execute("INSERT INTO items (name) VALUES (?)", (item,))

    conn.commit()
    conn.close()

def get_db_connection():
    conn = sqlite3.connect("data.db")
    conn.row_factory = sqlite3.Row  # Access rows as dictionaries
    return conn


def get_Items():
    conn = get_db_connection()
    list = conn.execute("SELECT * FROM items").fetchall()
    conn.close()
    return list

def add_Item(item):
    conn = get_db_connection()
    conn.execute("INSERT INTO items (name) VALUES (?)", (item,))
    conn.commit()
    conn.close()

def delete_item(id):
    conn = get_db_connection()
    list = conn.execute("DELETE FROM items WHERE id=?", (id,))
    conn.commit()
    conn.close()
