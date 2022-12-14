from requests_html import HTMLSession
import time
import pandas as pd
import pymysql


s = HTMLSession()

url = f'https://www.google.co.nz/search?q=google+weather+Mahurangi'

r = s.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'})

weatherlist = []

now = r.html.find('div.VQF4g', first=True).find('div#wob_dts', first=True).text
temp = r.html.find('span#wob_tm', first=True).text
unit = r.html.find('div.vk_bk.wob-unit span.wob_t', first=True).text
desc = r.html.find('div.VQF4g', first=True).find('span#wob_dc', first=True).text

datenow = time.strftime('%d-%b')



weather = {
    
    'temp': temp,
    'unit': unit,
    'desc': desc,
    'now': now,
    'date': datenow 
}
weatherlist.append(weather)

db = pymysql.connect(host='20.214.188.216', port=3306, user='root', password='Wx123456.', db='aquadatabase', charset='utf8')
cursor = db.cursor()

sql = "insert into aquadatabase.web_sc values (%s,'%s','%s','%s','%s')"%(temp, unit, desc, now,datenow)
cursor.execute(sql)
  
db.commit()
cursor.close()
db.close()

print(temp)
print(unit)
print(desc)
print(now)
print(datenow)




df = pd.DataFrame(weatherlist)


df.to_csv('weatherlist.csv')
