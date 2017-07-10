import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

def SendEmail(message, flag):
    msg = MIMEText(message, 'plain', 'utf-8')
    msg['From'] = formataddr(['Sender Name','account'])
    msg['To'] = formataddr(['Receiver Name','account'])
    if flag == 'Alert':
        msg['Subject'] = 'Content'
    else:
        msg['Subject'] = 'Content' 

    try:
        server = smtplib.SMTP('SMTP server of the sender', 25)
        server.login('account', "passwd")
        server.sendmail('title',['addr'], msg.as_string())
        print('Success')
        server.quit()
    except smtplib.SMTPException:
        print('Error')



if __name__ == '__main__':
    SendEmail("Hello world")
