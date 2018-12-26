import sqlite3
import os

class SQLite:
    def __init__(self, db_name, tb_name):
        self.database = db_name
        self.table = tb_name

    def open_db(self):
        conn = sqlite3.connect(self.database)
        c = conn.cursor()
        return conn, c

    def create_table(self):
        conn, c = self.open_db()
        sql_str = "CREATE TABLE IF NOT EXISTS " + self.table + \
            "(ID INTEGER PRIMARY KEY AUTOINCREMENT,\
            URL CHAR(255) ,\
            TITLE CHAR(255) NOT NULL)"
        c.execute(sql_str)
        conn.commit()
        conn.close()

    def insert_record(self, record):
        conn, c = self.open_db()
        sql_str = "insert into " + self.table \
                + "(URL, TITLE) VALUES (" + record + ")"
        c.execute(sql_str)
        conn.commit()
        conn.close()

    def select_all(self):
        conn, c = self.open_db()
        sql_str = "SELECT * FROM " + self.table
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
    
    sql = SQLite(s, t)
    
    sql.create_table()

    for r in [r1,r2,r3]:
        sql.insert_record(r)
    
    sql.select_all()

if __name__ == "__main__" :
    test()    
