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

    message = message_config()
    send_mail(message)
