import sqlite3

DATABASE_NAME = "database.db"

class Database:

    conn = None

    def __init__(self):
        self.conn = sqlite3.connect(DATABASE_NAME, check_same_thread=False)

    def create_tables(self):
        tables = [
            """CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                password TEXT NOT NULL,
                salt TEXT NOT NULL
            )
            """,
            """CREATE TABLE IF NOT EXISTS user_sessions(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                token TEXT NOT NULL,
                FOREIGN KEY (user_id)
                    REFERENCES users (id)
                        ON DELETE CASCADE
                        ON UPDATE NO ACTION
            )
            """,
            """CREATE TABLE IF NOT EXISTS products(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                price REAL NOT NULL
            )
            """,
            """CREATE TABLE IF NOT EXISTS carts(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                product_id INTEGER,
                FOREIGN KEY (user_id)
                    REFERENCES users (id)
                        ON DELETE CASCADE
                        ON UPDATE NO ACTION,
                FOREIGN KEY (product_id)
                    REFERENCES products (id)
                        ON DELETE CASCADE
                        ON UPDATE NO ACTION
            )
            """
        ]

        cursor = self.conn.cursor()
        print (cursor)
        for table in tables:
            cursor.execute(table)

# Import db in whichever file requires it. 
# Hopefully this will ensure one connection to database.
db = Database()