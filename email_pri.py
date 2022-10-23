from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.image import MIMEImage
import os

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
# US english
LANGUAGE = "en-US,en;q=0.5"

mail_host = "smtp.qq.com"
mail_user = "1006075208@qq.com"
mail_pass = "vzgmgbdioztvbcdd"


sender = '1006075208@qq.com'
receivers = ['jocker.xw@gmail.com']

def get_weather_data(url):
    url = f'https://www.google.com/search?q=google+weather+Mahurangi'
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE
    html = session.get(url)
    # create a new soup
    soup = bs(html.text, "html.parser")
    # store all results on this dictionary
    result = {}
    # extract region
    result['region'] = soup.find("div", attrs={"id": "wob_loc"}).text
    # extract temperature now
    result['temp_now'] = soup.find("span", attrs={"id": "wob_tm"}).text
    # get the day and hour now
    result['dayhour'] = soup.find("div", attrs={"id": "wob_dts"}).text
    # get the actual weather
    result['weather_now'] = soup.find("span", attrs={"id": "wob_dc"}).text
    # get the precipitation
    result['precipitation'] = soup.find("span", attrs={"id": "wob_pp"}).text
    # get the % of humidity
    result['humidity'] = soup.find("span", attrs={"id": "wob_hm"}).text
    # extract the wind
    result['wind'] = soup.find("span", attrs={"id": "wob_ws"}).text
    # get next few days' weather
    next_days = []
    days = soup.find("div", attrs={"id": "wob_dp"})
    for day in days.findAll("div", attrs={"class": "wob_df"}):
        # extract the name of the day
        day_name = day.findAll("div")[0].attrs['aria-label']
        # get weather status for that day
        weather = day.find("img").attrs["alt"]
        temp = day.findAll("span", {"class": "wob_t"})
        # maximum temparature in Celsius, use temp[1].text if you want fahrenheit
        max_temp = temp[0].text
        # minimum temparature in Celsius, use temp[3].text if you want fahrenheit
        min_temp = temp[2].text
        next_days.append({"name": day_name, "weather": weather, "max_temp": max_temp, "min_temp": min_temp})
    # append to result
    result['next_days'] = next_days
    return result
def message_config(r):


    mail_msg = """
        <h2>%s</h2>
        
        
    """%r
    content = MIMEText(mail_msg, 'html', 'utf-8')
    message = MIMEMultipart()
    message.attach(content)
    message['From'] = Header("Aqua", 'utf-8')
    message['To']   = Header("cutomer", 'utf-8')
    message['Subject'] = Header('data_scraping', 'utf-8')

    file_name = 'temperature_data_test.csv'
    file_path = os.path.join(file_name)
    xlsx = MIMEApplication(open(file_path, 'rb').read())
    xlsx["Content-Type"] = 'application/octet-stream'
    xlsx.add_header('Content-Disposition', 'attachment', filename=file_name)
    message.attach(xlsx)
    
    image1_name = 'ph.jpg'
    image1_path = os.path.join(image1_name)
    
    att3=MIMEImage(open(image1_path,'rb').read())
    att3["Content-Type"]='application/octet-stream'
    
    att3.add_header('Content-Disposition', 'attachment', filename=image1_name)
    message.attach(att3)
    
    image2_name = 'temp.jpg'
    image2_path = os.path.join(image2_name)
    
    att2=MIMEImage(open( image2_path,'rb').read())
    att2["Content-Type"]='application/octet-stream'
    att2.add_header('Content-Disposition', 'attachment', filename=image2_name)
    message.attach(att2)
    
    return message

def send_mail(message):

    try:
        smtpObj = smtplib.SMTP_SSL(mail_host)
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())

    except Exception as e:
        print(e)
    

if __name__ == "__main__":
    URL = "https://www.google.com/search?q=google+weather+Mahurangi"
    import argparse
    parser = argparse.ArgumentParser(description="Quick Script for Extracting Weather data using Google Weather")
    parser.add_argument("region", nargs="?", help="""Region to get weather for, must be available region.
                                        Default region is Mahurangi""", default="Mahurangi")
    # parse arguments
    args = parser.parse_args()
    region = args.region
    if region:
        region = region.replace(" ", "+")
        URL += f"+{region}"
    # get data
    data = get_weather_data(URL)
    # print data
    t = ''
    t_w = ("Weather for:" + data["region"] + "\n")
    t_d = ("Now:" + data["dayhour"] + "\n")
    t_t = (f"Temperature now: {data['temp_now']}°C \n")
    t_d1 = ("Description:" + data['weather_now'] +"\n")
    t_p = ("Precipitation:" + data["precipitation"] +"\n")
    t_h = ("Humidity:" +  data["humidity"] + "\n")
    t_w1 = ("Wind:" +  data["wind"] + "\n")
    t_wp = ("Weather prediction for the next 7 days:" + "\n")
    t = t_w + t_d + t_t + t_d1 + t_p + t_h + t_w1 + t_wp
    t1 = ''
    for dayweather in data["next_days"]:
        t1 = t1 + ("="*40 + dayweather["name"] + "="*40 + "\n")
        t1 = t1 + ("Description:" + dayweather["weather"] + "\n")
        t1 = t1 + (f"Max temperature: {dayweather['max_temp']}°C \n")
        t1 = t1 + (f"Min temperature: {dayweather['min_temp']}°C \n")
    
    t_r = t + t1
    message = message_config(t_r)
    send_mail(message)
        
