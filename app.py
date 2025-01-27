from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

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

init_db()


@app.route('/', methods=['GET'])
def index():  # put application's code here
    conn = get_db_connection()
    list = conn.execute("SELECT * FROM items").fetchall()
    conn.close()
    return render_template('index.html', list=list)

@app.route('/', methods=['POST'])
def add():
    item = request.form['item']
    conn = get_db_connection()
    conn.execute("INSERT INTO items (name) VALUES (?)", (item,))
    conn.commit()
    conn.close()
    return index()

@app.route('/complete', methods=['GET'])
def complete():
    id = request.args['id']
    print(id)
    conn = get_db_connection()
    list = conn.execute("DELETE FROM items WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return index()

if __name__ == '__main__':
    app.run()
