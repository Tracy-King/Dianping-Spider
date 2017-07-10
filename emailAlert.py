import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

def SendEmail(message, flag):
    msg = MIMEText(message, 'plain', 'utf-8')
    msg['From'] = formataddr(['163mail','account'])
    msg['To'] = formataddr(['qqmail','account'])
    if flag == 'Alert':
        msg['Subject'] = 'DianpingSpiderAlert'
    else:
        msg['Subject'] = 'DianpingSpiderFinished' 

    try:
        server = smtplib.SMTP('smtp.163.com', 25)
        server.login('account', "passwd")
        server.sendmail('title',['addr'], msg.as_string())
        print('Success')
        server.quit()
    except smtplib.SMTPException:
        print('Error')



if __name__ == '__main__':
    SendEmail("Hello world")
