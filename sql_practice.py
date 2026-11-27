import sqlite3

conn = sqlite3.connect(":memory:")
users_test = [("Аня", "Москва"),
              ("Боря", "Питер"),
              ("Ваня", "Москва"),
              ("Галя", "Казань")]

orders_test = [(1, 3000, "paid"),
               (1, 4000, "paid"),
               (1, 10000, "cancelled"),
               (2, 1500, "paid"),
               (3, 2000, "paid"),
               (3, 5000, "cancelled")]

conn.executescript('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        city TEXT
    )
''')
conn.executescript('''
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY,
        user_id INTEGER NOT NULL,
        amount INTEGER,
        status TEXT,
        FOREIGN KEY (user_id) REFERENCES users (id)
    )
''')

conn.executemany('''
    INSERT INTO users (name, city)
    VALUES (?, ?)
''', users_test)
conn.executemany('''
    INSERT INTO orders (user_id, amount, status)
    VALUES (?, ?, ?)
''', orders_test)

print(conn.execute('''SELECT users.name FROM users LEFT JOIN orders ON users.id = orders.user_id WHERE orders.id IS NULL''').fetchall())
