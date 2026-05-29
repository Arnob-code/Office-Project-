import sqlite3
import os

# folder create
os.makedirs("database", exist_ok=True)

# database path
db_path = "database/save_data.db"

# connect
conn = sqlite3.connect(db_path)

cursor = conn.cursor()

# table create
cursor.execute("""

CREATE TABLE IF NOT EXISTS users (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    first_name TEXT,
    last_name TEXT,
    email TEXT,
    password TEXT

)

""")

conn.commit()

print("Database Connected")