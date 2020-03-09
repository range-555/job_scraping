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
cursor.execute("SELECT * FROM contents")
rows = cursor.fetchall()

for row in rows:
    company_name = description = need_skills = place = work_hours = form = salary = holiday = ""
    content_page = BeautifulSoup(str(row[1]), "html.parser")
    company_name = content_page.find(class_ = "head_title").find('h1').text
    salary = content_page.find('tr', id = "salary").text
    table_tr = content_page.find_all('tr')
    for i in table_tr:
        if (i.find('th') is not None):
            if '仕事内容' in i.find('th').text:
                description = i.find('td').text.replace('"','""')
            elif '対象となる方' in i.find('th').text:
                need_skills = i.find('td').text.replace('"','""')
            elif '勤務地' in i.find('th').text:
                place = i.find('td').text.replace('"','""')            
            elif '勤務時間' in i.find('th').text:
                work_hours = i.find('td').text.replace('"','""')
            elif '雇用形態' in i.find('th').text:
                form = i.find('td').text.replace('"','""')
            elif '休日・休暇' in i.find('th').text:
                holiday = i.find('td').text.replace('"','""')
    try:
        sqlupdate = 'UPDATE contents SET company_name = "' + company_name + '",description = "' + description + '",need_skills = "' + need_skills +'",place = "' + place +'",work_hours = "' + work_hours +'",form = "' + form + '",salary = "' + salary + '",holiday = "' + holiday + '" WHERE id = "' + str(row[0]) + '";'
        cursor.execute(sqlupdate)
        connection.commit()
    except Exception as e:
        connection.rollback()
        raise e

cursor.close()
connection.close()