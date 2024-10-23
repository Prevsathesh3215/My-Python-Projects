##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


import datetime as dt
import smtplib
import pandas as pd
import random
letters = ['letter_1.txt', 'letter_2.txt', 'letter_3.txt']

now = dt.datetime.now()
my_email = "shabadabadingdongprevin@gmail.com"
password = "lowx lxcx wacg kmgq"

df = pd.read_csv('birthdays.csv')

for i in range(len(df) - 1):
    if now.day == df.loc[i, 'day'] and now.month == df.loc[i, 'month']:
        letter_choice = random.choice(letters)
        with open(letter_choice, 'r') as fd:
            letter_data = fd.read()

        letter_data = letter_data.replace('[NAME]', df.loc[i, 'name'])

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=df.loc[i, 'email'],
                                msg=f"Subject: HAPPY BIRTHDAY!\n\n{letter_data}")








