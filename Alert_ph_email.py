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


  sql = "select ph from web_ph;"
  cursor.execute(sql)
  results = cursor.fetchall()

  for i in results:

      for m in i:

          water_temps.append(m)

  db.commit()
  cursor.close()
  db.close()
  water_temps_int = list(map(float, water_temps))
  
  w = water_temps_int[-1] 
  r = ''
  if w < 4:
    r = r + ("Now the real-time PH is too low, please pay attention to the safety of farmers")
  if w > 8:
    r = r + ("Now the real-time PH is too high, please pay attention to the safety of farmers")
  message = message_config(r)
  send_mail(message)
