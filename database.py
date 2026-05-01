import sqlite3

DB = "logistics.db"

def connect():
    return sqlite3.connect(DB)

def create_tables():
    conn = connect()
    c = conn.cursor()

    # USERS (Admin, Staff, Driver)
    c.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        password TEXT,
        role TEXT
    )
    """)

    # SHIPMENTS
    c.execute("""
    CREATE TABLE IF NOT EXISTS shipments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        order_number TEXT,
        sender TEXT,
        receiver TEXT,
        item TEXT,
        status TEXT,
        driver_id INTEGER
    )
    """)

    # INVENTORY
    c.execute("""
    CREATE TABLE IF NOT EXISTS inventory (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        item_name TEXT,
        quantity INTEGER,
        warehouse TEXT
    )
    """)

    # VEHICLES
    c.execute("""
    CREATE TABLE IF NOT EXISTS vehicles (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        capacity INTEGER,
        status TEXT
    )
    """)

    # DRIVERS
    c.execute("""
    CREATE TABLE IF NOT EXISTS drivers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        phone TEXT
    )
    """)

    # LOGS
    c.execute("""
    CREATE TABLE IF NOT EXISTS logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        action TEXT,
        user TEXT
    )
    """)

    conn.commit()
    conn.close()