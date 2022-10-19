import smtplib
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import os



mail_host = "smtp.qq.com"
mail_user = "1006075208@qq.com"
mail_pass = "vzgmgbdioztvbcdd"


sender = '1006075208@qq.com'
receivers = ['1006075208@qq.com']


def message_config():


    mail_msg = """
        <h2>hello</h2>
        
        
    """
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
    
    att3=MIMEImage(open('ph.jpg','rb').read())
    att3["Content-Type"]='application/octet-stream'
    att3["Content-Disposition"] = 'attachment; filename="fujian3.jpg"'
    message.attach(att3)
    att2=MIMEImage(open('temp.jpg','rb').read())
    att2["Content-Type"]='application/octet-stream'
    att2["Content-Disposition"] = 'attachment; filename="fujian3.jpg"'
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

    message = message_config()
    send_mail(message)
