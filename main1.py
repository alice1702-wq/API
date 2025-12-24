import sqlite3

conn = sqlite3.connect("urls.db")
cur = conn.cursor()

cur.execute("SELECT * FROM urls;")

rows = cur.fetchall()

for row in rows:
    print(rows)