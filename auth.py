from database import connect

def login(username, password):
    conn = connect()
    c = conn.cursor()

    c.execute("SELECT role FROM users WHERE username=? AND password=?", (username, password))
    result = c.fetchone()

    conn.close()
    return result[0] if result else None


def register(username, password, role):
    conn = connect()
    c = conn.cursor()

    c.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
              (username, password, role))

    conn.commit()
    conn.close()