import smtplib

my_email = "shabadabadingdongprevin@gmail.com"
password = "lowx lxcx wacg kmgq"


with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="udemytest@hotmail.com",
                        msg="Subject: A message from your lover\n\nHello mine lover, how fare thee? I am sending "
                            "this from a code I wrote. Instead of using normal Gmail,"
                            "I can use code to do it and automate it instead. How brilliant!"
                            "This is as amazing as you, my sunshine. You are beautiful like the red rose"
                            "in the glittering evening sky, as calming as the waves that break on a pearly white "
                            "seashore, as kind and gentle as a soothing breeze. I wish to only be in your embrace,and feel"
                            "your heart beating in unison with mine, love. Oh, how my heart yearns for you! I will see your soon, "
                            "my darling. Till then, keep me in your memory.\nYour beloved, Sathesh")


# import datetime as dt
# import smtplib, random
#
# with open('quotes.txt', 'r') as fd:
#     data = fd.read()
#     quote = data.splitlines()
#     quote_size = len(quote)
#


# now = dt.datetime.now()
# # year = now.year
# # month = now.month
# #
# # dateofbirth = dt.datetime(year=1999, month=10, day=29)
# # print(dateofbirth)
# # print(dateofbirth.year, dateofbirth)
#
# my_email = "shabadabadingdongprevin@gmail.com"
# password = "lowx lxcx wacg kmgq"
#
# if now.weekday() == 5:
#
#     with smtplib.SMTP("smtp.gmail.com") as connection:
#         connection.starttls()
#         connection.login(user=my_email, password=password)
#         connection.sendmail(from_addr=my_email, to_addrs="fausty.alex99@gmail.com",
#                             msg=f"Subject: A Quote for You\n\n{random.choice(quote)}\nHave a great day ahead!")
#
#
