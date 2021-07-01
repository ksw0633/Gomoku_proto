import sqlite3
import json
import requests

conn = sqlite3.connect('paired_comments.db')
cursor = conn.cursor()

def create_table():
    cursor.execute("""CREATE TABLE IF NOT EXISTS paired_comments(
                body STRING,
                score INTEGER,
                parent_id STRING, 
                subreddit STRING,
                link_id STRING,
                created_utc INTEGER,
                id STRING,
                parent_body STRING
    )""")

def format_body(body):
    body =  body.replace("\n", " newlinechar ").replace("\r", "newlinechar").replace('"',"'")
    return body

def shitpost(body):
    if len(body.split(' ')) > 100 or len(body.split(' ')) < 1:
        return False
    elif len(body) > 1000:
        return False
    else:
        return True


row_count = 1; 
f = open("./paired_comments", encoding = 'utf-8')
create_table()
for row in f:
    row = json.loads(row)
    body = row['body']
    score = int(row['score'])
    parent_id = row['parent_id']
    subreddit = row['subreddit']    
    link_id = row['link_id']
    created_utc = int(row['created_utc'])
    id = row['id']
    parent_body = row['parent_body']
    body = format_body(body)
    parent_body = format_body(parent_body)
    shitpost(body)
#    print(body+" "+score+" "+parent_id+" "+subreddit+" "+link_id+" "+created_utc+ " "+ id +" "+parent_body)
    query = """INSERT INTO paired_comments(body, score, parent_id, subreddit, link_id, created_utc, id, parent_body) VALUES (?, ?, ?, ?, ?, ?, ?, ?);"""
#    query = """INSERT INTO paired_comments(body, score, parent_id, subreddit, link_id, created_utc, id, parent_body) VALUES ();"""
    cursor.execute(query,(str(body), score, str(parent_id), str(subreddit), str(link_id), created_utc, id, str(parent_body)))
conn.commit()
conn.close()
