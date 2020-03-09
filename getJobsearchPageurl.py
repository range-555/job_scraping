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

cursor = connection.cursor()

target_urls = {
    "フロントエンド": "Frontend_url",
    "サーバーサイド": "Serverside_url",
    "ゲーム プログラマー": "Game_url"
    }

def register_to_db(search, url):
    try:
        cursor.execute("INSERT INTO urls(search, url) VALUES (%(search)s, %(url)s)", {'search':search, 'url':url})
        connection.commit()
    except Exception as e:
        connection.rollback()
        raise e

def get_urls(job_search_list):
    for i in job_search_list:
        if 'tab__pr' in i['href']:
            sleep(3)
            response_pr = req.urlopen(i['href'])
            pr_page = BeautifulSoup( response_pr, "html.parser")
            register_to_db(search,pr_page.find(class_ = '_canonicalUrl')['href'])
        else:
            register_to_db(search, i['href'])


for search,target_url in target_urls.items():
    sleep(3)
    response = req.urlopen(target_url)
    search_result_page = BeautifulSoup(response, "html.parser")
    job_search_list = search_result_page.find_all(class_ = 'btnJob03 _JobListToDetail')
    get_urls(job_search_list)
    while search_result_page.find('a', class_='pagenationNext') is not None:
        sleep(3)
        response = req.urlopen(search_result_page.find('a', class_='pagenationNext')['href'])
        search_result_page = BeautifulSoup(response, "html.parser")
        job_search_list = search_result_page.find_all(class_ = 'btnJob03 _JobListToDetail')
        get_urls(job_search_list)

cursor.close()
connection.close()