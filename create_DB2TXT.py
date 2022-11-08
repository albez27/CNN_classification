import MySQLdb
from preprocess_text import preprocess_text

connection = MySQLdb.connect(host="localhost",
                             user="root",
                             passwd="root",
                             db="tweets")
cur = connection.cursor()
query = "SELECT ttext FROM sentiment"
cur.execute(query)
with open('Data/tweets.txt', 'w', encoding='utf-8') as w_file:
    for row in cur.fetchall():
        p_tweet = preprocess_text(row[0])
        print(p_tweet, file=w_file)
connection.close()