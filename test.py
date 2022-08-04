import pymysql

conn = pymysql.connect(host="localhost", user="root", password="123456789", db="cctv_db",
                       charset="utf8")
curs = conn.cursor()
curs2 = conn.cursor()

sql = """insert into all_in_one(id, action, time)
         values(%s, %s, now())"""
sql2 = """select distinct id, action from all_in_one"""

curs2.execute(sql2)
rows = curs2.fetchall()
a = []

print(rows)

for i in range(len(rows)):
    a.append(rows[i])

print(a)

if ('1', 'a') not in a:
    curs.execute(sql, (1, 'a'))


conn.commit()


