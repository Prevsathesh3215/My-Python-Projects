
import requests as rq
import datetime as dt
import os

#GET TODAY'S DATE
today_date = dt.datetime.strftime(dt.datetime.now(), '%d/%m/%Y')
today_time = dt.datetime.strftime(dt.datetime.now(), '%H:%M:%S')




#GET EXERCISE DATA

exercise_endpoint = os.environ.get('ENDPOINT')
headers = {
    'x-app-id': os.environ.get('APP_ID'),
    'x-app-key': os.environ.get('API_KEY')
}

input_text = input("Tell me what exercise you did today: ")
params = {
    'query':input_text,
    'weight_kg': 78,
    'height_cm': 182,
    'age': 25,
}

resp = rq.post(url=exercise_endpoint, json=params, headers=headers)
data = resp.json()

data_to_post = {
    'workout': {
        'date': today_date,
        'time': today_time,
        'duration': data['exercises'][0]['duration_min'],
        'exercise': data['exercises'][0]['name'].title(),
        'calories': data['exercises'][0]['nf_calories'],
    }
}




#POST TO GOOGLE SHEETS

sheety_endpoint = os.environ.get('SHEETY_ENDPOINT')

sheety_header = {
    'Authorization': 'Bearer yabadabadoooey31682012313123012312'
}

post_rows = rq.post(url=sheety_endpoint, json=data_to_post, headers=sheety_header)
# print(post_rows.text)

if post_rows.status_code == 200:
    print('Alright, your input has been recorded. Thank you!')

else:
    print(post_rows.raise_for_status())