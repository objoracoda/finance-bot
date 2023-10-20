import sqlite3
from sqlite3 import Error


def sql_connection():
    try:
        con = sqlite3.connect('db/expense.db')
        return con
    except Error:
        print(Error)
 

def sql_table(con):
    cursor = con.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS expense(title text, amount integer)')
    con.commit()


def connect():
    con = sql_connection()
    sql_table(con)
    sql_insert(con)
    return con


def sql_insert(con):
    cursor = con.cursor()
    info = cursor.execute('SELECT * FROM expense WHERE title=?', ("дорога",)).fetchone()
    if not info:
        cursor.execute('INSERT INTO expense(title, amount) VALUES("дорога",0),("кафе",0),("личное",0),("прочее",0)')
    con.commit()
    sql_fetch(con)


def sql_update(con,entities):
    print(entities)
    cursor = con.cursor()
    cursor.execute('UPDATE expense SET amount = amount + ? where title = ?', entities)
    con.commit()
    sql_fetch(con)


def sql_fetch(con):
    print("================")
    cursor = con.cursor()
    cursor.execute('SELECT * FROM expense')
    rows = cursor.fetchall()
    for row in rows:
        print(row)


def sql_show_table(con):
    cursor = con.cursor()
    cursor.execute('SELECT * FROM expense')
    rows = cursor.fetchall()
    return rows


def sql_new_mounth(con):
    cursor = con.cursor()
    cursor.execute('UPDATE expense SET amount = 0')
    con.commit()
    sql_fetch(con)