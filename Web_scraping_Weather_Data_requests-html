from requests_html import HTMLSession
import time
import pandas as pd


s = HTMLSession()

url = f'https://www.google.com/search?q=google+weather+Mahurangi'

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




df = pd.DataFrame(weatherlist)


df.to_csv('weatherlist.csv')
