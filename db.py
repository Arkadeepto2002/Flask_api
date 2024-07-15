# import sqlite3
import pymysql
# conn = sqlite3.connect("book.sqlite")
conn = pymysql.connect(
    host='sql8.freesqldatabase.com',
    database='sql8719773',
    user='sql8719773',
    password='lUIZbP82wU',
    port= 3306,
    cursorclass= pymysql.cursors.DictCursor
)
cursor = conn.cursor()

sql_query = """CREATE TABLE book(
    id INT AUTO_INCREMENT PRIMARY KEY ,
    author VARCHAR(255) NOT NULL,
    language VARCHAR(255) NOT NULL,
    title VARCHAR(255) NOT NULL
)"""

# sql_query="""DROP TABLE book"""
cursor.execute(sql_query)
conn.close()