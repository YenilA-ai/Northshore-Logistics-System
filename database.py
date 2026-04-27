import sqlite3

DB_NAME = "app.db"

def connect():
    return sqlite3.connect(DB_NAME)

def create_table():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS records (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        email TEXT
    )
    """)

    conn.commit()
    conn.close()

def insert_record(name, age, email):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO records (name, age, email)
    VALUES (?, ?, ?)
    """, (name, age, email))

    conn.commit()
    conn.close()

def get_all_records():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM records")
    rows = cursor.fetchall()

    conn.close()
    return rows

def update_record(record_id, name, age, email):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE records
    SET name = ?, age = ?, email = ?
    WHERE id = ?
    """, (name, age, email, record_id))

    conn.commit()
    conn.close()

def delete_record(record_id):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    DELETE FROM records
    WHERE id = ?
    """, (record_id,))

    conn.commit()
    conn.close()

def search_records(keyword):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM records
    WHERE name LIKE ?
    """, ('%' + keyword + '%',))

    rows = cursor.fetchall()
    conn.close()
    return rows