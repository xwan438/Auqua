import pandas as pd
import numpy as np
import matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as md
from datetime import datetime, timedelta
import datetime
import seaborn as sns
from pylab import rcParams
import  pymysql
import smtplib
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.image import MIMEImage
import os

mail_host = "smtp.qq.com"
mail_user = "1006075208@qq.com"
mail_pass = "vzgmgbdioztvbcdd"


sender = '1006075208@qq.com'
receivers = ['jocker.xw@gmail.com']
def message_config(r):


    mail_msg = """
        <body>%s</body>
        
        
    """%r
    content = MIMEText(mail_msg, 'html', 'utf-8')
    message = MIMEMultipart()
    message.attach(content)
    message['From'] = Header("Aqua", 'utf-8')
    message['To']   = Header("cutomer", 'utf-8')
    message['Subject'] = Header('data_scraping', 'utf-8')

    
    
   
    
    return message

def send_mail(message):

    try:
        smtpObj = smtplib.SMTP_SSL(mail_host)
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())

    except Exception as e:
        print(e)
if __name__ == "__main__":
  water_temps = []
  db = pymysql.connect(host='20.214.188.216', port=3306, user='root', password='Wx123456.', db='aquadatabase',
                       charset='utf8')
  cursor = db.cursor()


  sql = "select temp from web_sc;"
  cursor.execute(sql)
  results = cursor.fetchall()

  for i in results:

      for m in i:

          water_temps.append(m)

  db.commit()
  cursor.close()
  db.close()
  water_temps_int = list(map(int, water_temps))
  water_temps_int_1 = []
  for i in water_temps_int:
      a = int((i - 32)/1.8)
      water_temps_int_1.append(a)
  w = water_temps_int_1[-1] 
  r = ''
  if w < 12:
    r = r + ("Now the real-time temperature is too low, please pay attention to the safety of farmers")
    message = message_config(r)
    send_mail(message)
  if w > 35:
    r = r + ("Now the real-time temperature is too high, please pay attention to the safety of farmers")
    message = message_config(r)
    send_mail(message)
  
  

