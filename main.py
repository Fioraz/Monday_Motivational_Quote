# # Testing Python Mail
#
# import smtplib
#
# my_email = "your_email@gmail.com"
# password = "ernejrhdckhnmfdk"  # App Password - gmail account
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="receiver's_email@gmail.com",
#         msg="Subject:Testing Python Mail\n\nHello, this is the email body"
#     )
#

# Monday Motivational Quote Email

import smtplib
import datetime as dt
import random

data_dict = {}
my_email = "your_email@gmail.com"
password = "ernejrhdckhnmfdk"
now = dt.datetime.now()

if now.weekday() == 1:
    with open("quotes.txt") as quotes_file:
        quotes = quotes_file.readlines()
        quote = random.choice(quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="receiver's_email@gmail.com",
            msg=f"Subject: Monday Motivation!\n\n{quote}"
        )
