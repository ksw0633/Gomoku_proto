import sqlite3
import json
import requests

conn = sqlite3.connect('paired_comments.db')
cursor = conn.cursor()  

with conn:
    cursor.execute("SELECT * FROM paired_comments LIMIT 10")
    print(cursor.fetchall())