import requests as rq
import datetime as dt
import smtplib
import time

LATITUDE = 3.054830
LONGITUDE = 101.786377
now = dt.datetime.now()
my_email = 'shabadabadingdongprevin@gmail.com'
password = "lowx lxcx wacg kmgq"

latitude_range = [n for n in range(round(LATITUDE) - 10,
                                   round(LATITUDE) + 10, 1)]
longitude_range = [n for n in range(round(LONGITUDE) - 10,
                                    round(LONGITUDE) + 10, 1)]



parameters = {
    'lat': LATITUDE,
    'lng': LONGITUDE,
    'formatted':0,
}

resp_one = rq.get(url='http://api.open-notify.org/iss-now.json')
resp_one.raise_for_status()

data_iss = resp_one.json()
iss_latitude = data_iss['iss_position']['latitude']
iss_longitude = data_iss['iss_position']['longitude']

resp_two = rq.get(url='https://api.sunrise-sunset.org/json',
                  params=parameters)
resp_two.raise_for_status()
data = resp_two.json()


sunrise_hour = int((data['results']['sunrise'].split('T'))[1].split(':')[0])
sunset_hour = int((data['results']['sunset'].split('T'))[1].split(':')[0])

while True:
    time.sleep(60)
    if now.hour >= sunset_hour or now.hour <= sunrise_hour:
        if iss_latitude in latitude_range and iss_longitude in longitude_range:
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(from_addr=my_email,
                                    to_addrs='udemytest@hotmail.com',
                                    msg='Subject: ISS ALERT!\n\nThe ISS is above you, look up!')

