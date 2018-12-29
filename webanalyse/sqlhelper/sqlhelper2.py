import sqlite3
import os

class SQLite:
    """A simple class for use sqlite3.
    
    """
    def __init__(self, db_name, tb_name):
        self.database = db_name
        self.table = tb_name
        self.conn = sqlite3.connect(self.database)
        self.c = self.conn.cursor()
        
    def create_table(self):
        sql_statement = "CREATE TABLE IF NOT EXISTS " + self.table + \
            "(ID INTEGER PRIMARY KEY AUTOINCREMENT,\
            URL CHAR(255) ,\
            TITLE CHAR(255) NOT NULL)"
        self.c.execute(sql_statement)
        self.conn.commit()

    def insert_record(self, record):
        sql_statement = "insert into " + self.table \
                + "(URL, TITLE) VALUES (" + record + ")"
        self.c.execute(sql_statement)
        self.conn.commit()

    def select_all(self):
        sql_statement = "SELECT * FROM " + self.table
        cursor = self.c.execute(sql_statement)
        for c in cursor:
            print(c[0], c[1], c[2])

    def close(self):
        self.conn.close()

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
    sql.close()

if __name__ == "__main__" :
    test()    
