import sqlite3
import  pandas as pd

conn =  sqlite3.connect('paired_comments.db')
cursor =    conn.cursor()

buff = 5000
last_unix = 0 
cur_length = buff
counter = 0
test_done = False

while cur_length == buff:
    query = "SELECT * FROM paired_comments WHERE created_utc > {} AND parent_body NOT NULL ORDER BY created_utc ASC LIMIT {}".format(last_unix, buff)
    dataframe = pd.read_sql(query ,conn)
    last_unix = dataframe.tail(1)['created_utc'].values[0]
    cur_length = len(dataframe)
    if not test_done:
        with open("test.from", 'a', encoding='utf-8') as f:
            for content in dataframe['parent_body'].values:
                f.write(str(content) + '\n')
        with open("test.to", 'a', encoding='utf-8') as f:
            for content in dataframe['body'].values:
                f.write(str(content) + '\n')
        test_done = True
    else:
        with open("train.from", 'a', encoding='utf-8') as f:
            for content in dataframe['parent_body'].values:
                f.write(str(content) + '\n')
        with open("train.to", 'a', encoding='utf-8') as f:
            for content in dataframe['body'].values:
                f.write(str(content) + '\n')
    counter += 1
    if counter % 20 == 0:
        print(counter * buff, 'rows completed')