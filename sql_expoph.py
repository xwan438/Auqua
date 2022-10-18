import  pymysql
datalist = []
db = pymysql.connect(host='20.214.188.216', port=3306, user='root', password='Wx123456.', db='aquadatabase',
                     charset='utf8')
cursor = db.cursor()


sql = "select ph from web_ph;"
cursor.execute(sql)
results = cursor.fetchall()

for i in results:

    for m in i:

        datalist.append(m)

db.commit()
cursor.close()
db.close()
print(datalist)
