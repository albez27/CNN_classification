import re
import MySQLdb


def preprocess_text(text):
    text = text.lower().replace("ё", "е")
    text = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', 'URL', text)
    text = re.sub('@[^\s]+', 'USER', text)
    text = re.sub('[^a-zA-Zа-яА-Я1-9]+', ' ', text)
    text = re.sub(' +', ' ', text)
    return text.strip()


connection = MySQLdb.connect(host="localhost",
                             user="root",
                             passwd="root",
                             db="tweets")
cur = connection.cursor()
cur.execute("SELECT ttext FROM sentiment")
with open('tweets.txt', 'w', encoding='utf-8') as w_file:
    for row in cur.fetchall():
        p_tweet = preprocess_text(row[0])
        print(p_tweet, file=w_file)
connection.close()
