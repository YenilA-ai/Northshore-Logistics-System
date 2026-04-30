import sqlite3

DB_NAME = "app.db"

def connect():
    return sqlite3.connect(DB_NAME)

def create_table():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS inventory (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        item_name TEXT NOT NULL,
        quantity INTEGER,
        location TEXT
    )
    """)

    conn.commit()
    conn.close()

def insert_record(item_name, quantity, location):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO inventory (item_name, quantity, location)
    VALUES (?, ?, ?)
    """, (item_name, quantity, location))

    conn.commit()
    conn.close()

def get_all_records():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM inventory")
    rows = cursor.fetchall()

    conn.close()
    return rows

def update_record(record_id, item_name, quantity, location):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE inventory
    SET item_name = ?, quantity = ?, location = ?
    WHERE id = ?
    """, (item_name, quantity, location, record_id))

    conn.commit()
    conn.close()

def delete_record(record_id):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM inventory WHERE id = ?", (record_id,))

    conn.commit()
    conn.close()

def search_records(keyword):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM inventory
    WHERE item_name LIKE ?
    """, ('%' + keyword + '%',))

    rows = cursor.fetchall()
    conn.close()
    return rows