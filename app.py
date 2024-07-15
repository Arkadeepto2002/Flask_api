from flask import Flask,request,jsonify
import json
import sqlite3
import pymysql
app = Flask(__name__)

def db_connection():
    conn = None
    try:
        # conn = sqlite3.connect("book.sqlite")
        conn = pymysql.connect(
        host='sql8.freesqldatabase.com',
        database='sql8719773',
        user='sql8719773',
        password='lUIZbP82wU',
        port= 3306,
        cursorclass= pymysql.cursors.DictCursor
        )
    # except sqlite3.Error as e:
    except pymysql.Error as e:
        print(e)
    return conn

@app.route('/')
def index():
    return "Perform GET and POST keys:(author,title and language) on \'route/book\' or perform GET,PUT or DELETE on \'route/book/id\'"

@app.route('/<name>')
def greet(name):
    return "Hello, "+name

@app.route('/book',methods=['GET','POST'])
def books():
    conn = db_connection()
    cursor = conn.cursor()
    if(request.method == 'GET'):
        cursor.execute("Select * from book")
        books = [ dict(id=row['id'],author=row['author'],language=row['language'],title=row['title'])for row in cursor.fetchall()]
        if books is not None:
            return jsonify(books)

    if(request.method == 'POST'):
        new_author = request.form['author']
        new_lang = request.form['language']
        new_title = request.form['title']
        
        sql_insert = """INSERT INTO  book (author, language, title) VALUES (%s,%s,%s)"""
        cursor.execute(sql_insert,(new_author,new_lang,new_title))
        conn.commit()
        return f"Book with id {cursor.lastrowid}: created successfully"
    conn.close()
    
@app.route('/book/<int:id>',methods= ['GET','PUT','DELETE'])
def single_book(id):
    conn = db_connection()
    cursor = conn.cursor()
    if request.method == 'GET':
        cursor.execute("SELECT * FROM book where id=%s",(id,))

        rows = cursor.fetchall()
        book = None
        for r in rows:
            book = rows
        if book is not None:
            return jsonify(book)
        else:
            return "Something is wrong"
    if request.method == 'PUT':

        new_author = request.form['author']
        new_lang = request.form['language']
        new_title = request.form['title']

        updated_book= {
            'id':id,
            'author':new_author,
            'language':new_lang,
            'title':new_title
        }
        cursor.execute("UPDATE book SET title=%s,author=%s,language=%s WHERE id=%s",(new_title,new_author,new_lang,id))
        conn.commit()
        return jsonify(updated_book)
    if request.method == 'DELETE':

        cursor.execute("DELETE FROM book where id=%s",(id,))
        conn.commit()
        return f"The book with id {id} has been deleted"
    conn.close()

if(__name__ == '__main__'):
    app.run()