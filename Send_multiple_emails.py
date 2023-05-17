import random
# import smtplib
import string
from email.message import EmailMessage
import datetime as dt
import time
import smtplib


def send_email(mail_counter):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("testcomm100qa@gmail.com", "gcynfimfvymxwzkh")
    msg = EmailMessage()
    msg['From'] = "testcomm100qa@gmail.com"
    msg['To'] = 'PattiF@7wn1tk.onmicrosoft.com'
    # random_str = ''.join(random.choices(string.ascii_lowercase, k=10))
    msg['Subject'] = "Mail After Password Change " + ' ' + str(mail_counter)
    msg.set_content("Mail After Password Change " + ' ' + str(mail_counter))
    print(" Message Sent to : PattiF@7wn1tk.onmicrosoft.com")
    s.send_message(msg)
    s.quit()


def send_email_at(send_new_time, mail_counter):
    time_now = dt.datetime.utcnow()
    time_now_timestamp = dt.datetime.timestamp(time_now)
    time.sleep(send_new_time.timestamp() - time_now_timestamp)
    send_email(mail_counter)
    print(str(mail_counter) + ' email sent')


if __name__ == '__main__':
    first_email_time = dt.datetime(2023, 3, 16, 15, 24, 0)
    interval = dt.timedelta(seconds=1 * 10)
    send_time = first_email_time
    counter = 0
    while counter < 50:
        send_email_at(send_time, counter + 1)
        send_time = send_time + interval
        counter = counter + 1

