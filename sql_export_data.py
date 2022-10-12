import  pymysql
datalist = []
db = pymysql.connect(host='20.214.188.216', port=3306, user='root', password='Wx123456.', db='aquadatabase',
                     charset='utf8')
cursor = db.cursor()


sql = "select temp from web_sc;"
cursor.execute(sql)
results = cursor.fetchall()

for i in results:

    for m in i:
        m = int(m)
        m = round((m - 32) / 1.8)
        datalist.append(m)

sql_units = "select temp from web_sc;"
cursor.execute(sql)
results = cursor.fetchall()

db.commit()
cursor.close()
db.close()
print(datalist)
