# # Testing Python Mail
#
# import smtplib
#
# my_email = "addinusha@gmail.com"
# password = "wmfeywuitgyjmnen"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="dinusha.diss@gmail.com",
#         msg="Subject:Testing Python Mail\n\nHello, this is the email body"
#     )
#

# Monday Motivational Quote Email

import smtplib
import datetime as dt
import random

data_dict = {}
my_email = "addinusha@gmail.com"
password = "wmfeywuitgyjmnen"
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
            to_addrs="dinusha.diss@gmail.com",
            msg=f"Subject: Monday Motivation!\n\n{quote}"
        )
