import sqlite3


def create_table(cmd):
    db = sqlite3.connect("proxy_data.dbf")
    cursor = db.cursor()
    cmd = '''CREATE table if not exists PROXY(
        id INTEGER primary key autoincrement,
        ip_address TEXT,
        port INTEGER,
        country TEXT,
        speed TEXT,
        type TEXT,
        anonymity TEXT,
        last_check TEXT
        )
        '''
    cursor.execute(cmd)
    db.close()


def insert_into_table(proxies):
    db = sqlite3.connect("proxy_data.dbf")
    cursor = db.cursor()
    cmd = '''INSERT into PROXY(ip_address, port, country, speed, type, anonymity, last_check) values(?,?,?,?,?,?,?)'''
    for row in list_of_proxies:
        cursor.execute(cmd, (row.ip_address, row.port, row.country, row.speed, row.type, row.anonymity, row.last_check))
    db.commit()
    db.close()


def select_table(request):
    db = sqlite3.connect("proxy_data.dbf")
    cursor = db.cursor()
    cursor.execute(request)
    print("=" * 50)
    db.close()


def research_proxy_by_country(request, country):
    db = sqlite3.connect("proxy_data.dbf")
    cursor = db.cursor()
    cursor.execute(request, (country,))
    print("=" * 50)
    for row in cursor:
        print("{}, {}, {}, {}, {}, {}, {}".format(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
    db.close()