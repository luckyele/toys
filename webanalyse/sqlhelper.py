import sqlite3
import os

def open_db(sql):
    conn = sqlite3.connect(sql)
    c = conn.cursor()
    return conn, c

def create_table_in(db_name, table_name):
    conn, c = open_db(db_name)
    sql_str = "CREATE TABLE IF NOT EXISTS " + table_name + \
            "(ID INTEGER PRIMARY KEY AUTOINCREMENT,\
            URL CHAR(255) NOT NULL,\
            TITLE CHAR(255) NOT NULL)"
    c.execute(sql_str)
    conn.commit()
    conn.close()

def insert_record(db_name, table_name, record):
    conn, c = open_db(db_name)
    sql_str = "insert into " + table_name \
                + "(URL, TITLE) VALUES (" + record + ")"
    c.execute(sql_str)
    conn.commit()
    conn.close()

def select_from(db_name, table_name):
    conn, c = open_db(db_name)
    sql_str = "select * from "+table_name
    cursor = c.execute(sql_str)
    for c in cursor:
        print(c[0], c[1], c[2])
    conn.close()


def test():
    s = "mytest.db"
    t = "web_con"
    
    r1 = "\"www.mct1.gov.cn\",\"title1\""
    r2 = "\"www.mct2.gov.cn\",\"title2\""
    r3 = "\"www.mct3.gov.cn\",\"title3\""
    
    create_table_in(s, t)
    
    for r in [r1,r2,r3]:
        insert_record(s,t,r)
    
    select_from(s,t)

if __name__ == "__main__" :
    test()    
