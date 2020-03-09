import urllib.request as req,urllib.parse
from bs4 import BeautifulSoup
from time import sleep
import mysql.connector as mydb

connection = mydb.connect(
  host = 'localhost',
  port = '3306',
  user = 'username',
  password = 'password',
  database = 'dbname'
)

def register_to_db(id,html,search,url):
    try:
        cursor.execute("INSERT INTO contents(html,search,url) VALUES (%(html)s, %(search)s, %(url)s)", {'html':html, 'search':search, 'url':url})
        connection.commit()
    except Exception as e:
        connection.rollback()
        raise

cursor = connection.cursor()
cursor.execute("SELECT * FROM urls")
target_urls = cursor.fetchall()

for row in target_urls:
    sleep(1)
    try:
        response = req.urlopen(row[2])
    except Exception as e:
        continue

    register_to_db(row[0],response.read(),row[1],row[2])

cursor.close()
connection.close()