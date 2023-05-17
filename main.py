import random
import smtplib
import string
from email.message import EmailMessage
from time import sleep


def send_email():
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("testcomm100qa@gmail.com", "gcynfimfvymxwzkh")
    email_id_list = [
        # 'divakar_mishra@7wn1tk.onmicrosoft.com',
        # 'AdeleV@7wn1tk.onmicrosoft.com',
        # 'HenriettaM@7wn1tk.onmicrosoft.com',
        # 'PattiF@7wn1tk.onmicrosoft.com',
        # 'JoniS@7wn1tk.onmicrosoft.com',
        # 'PradeepG@7wn1tk.onmicrosoft.com',
        # 'divakar@comm100indiadev.in',
        # 'anurag.kumar@comm100.com',
        # 'indiadev@comm100.com',
        'indiatest1@comm100.com'
    ]

    counter = 0
    while counter < 20:
        for email_id in email_id_list:
            msg = EmailMessage()
            msg['From'] = "testcomm100qa@gmail.com"
            msg['To'] = email_id
            random_str = ''.join(random.choices(string.ascii_lowercase, k=10))
            msg['Subject'] = "Test Email for Auto Distribution on Staging : " + str(counter+1)
            msg.set_content("Test Email for Auto Distribution body on Staging : " + str(counter+1))
            print(str(counter+1) + " Message Sent to :" + email_id)
            s.send_message(msg)
        sleep(2)
        counter = counter + 1
    s.quit()


if __name__ == '__main__':
    send_email()
