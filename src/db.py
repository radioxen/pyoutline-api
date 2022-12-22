import sqlite3 as sl

con = sl.connect('users.db')

with con:
    con.execute("""
        CREATE TABLE USER (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            key TEXT
        );
    """)
