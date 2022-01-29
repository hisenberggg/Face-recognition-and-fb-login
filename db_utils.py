from locale import currency
import sqlite3

def connect(dbname='test.db'):
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    return conn,cur


def createTable(conn,cur):
    cur.execute("""
        create table Data (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NAME TEXT,
            USERNAME TEXT,
            PASSWORD TEXT
        )
        """)
    conn.commit()

def insertData1(conn,cur,data_list):
    cur.executemany("INSERT INTO Data (NAME,USERNAME,PASSWORD) VALUES (?,?,?)",data_list)
    conn.commit()

def insertData(conn,cur,name,user,pwd):
    cur.execute("INSERT INTO Data (NAME,USERNAME,PASSWORD) VALUES (:name,:user,:pwd)",{'name':name,'user':user,'pwd':pwd})
    conn.commit()

def printData(conn,cur):
    cur.execute("SELECT * FROM Data")
    print(cur.fetchall())

def searchName(cur,name):
    cur.execute("SELECT count(*) FROM Data where NAME =:name",{'name':name})
    return True if cur.fetchone()[0] > 0 else False

def getCred(cur,name):
    cur.execute("SELECT USERNAME,PASSWORD FROM Data where NAME =:name",{'name':name})
    d = [(row[0],row[1]) for row in cur][0]
    return d[0],d[1]


if __name__=='__main__':
    conn,cur = connect()

    createTable(conn,cur)

    # data = [('Name1','test@gmail.com','test'),
    #         ('Name2',"testemail","testpass")]
    # insertData1(conn,cur,data)

    # print(searchName(conn,cur,'Name1'))

    printData(conn,cur)

    conn.close()
