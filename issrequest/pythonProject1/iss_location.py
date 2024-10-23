import requests as rq, time
headers = {
    'Accept': 'application/json'
}

while True:
    resp_one = rq.get(url='http://api.open-notify.org/iss-now.json')
    resp_one.raise_for_status()

    data_iss = resp_one.json()
    print(data_iss)
    iss_latitude = data_iss['iss_position']['latitude']
    iss_longitude = data_iss['iss_position']['longitude']

    resp_two = rq.get(
        url=f'https://api.geoapify.com/v1/geocode/reverse?lat={iss_latitude}&lon={iss_longitude}&apiKey=897e10506ff94f3c8582054e7998434b',
        headers=headers)
    data_location = resp_two.json()
    # print(data_location['features'][0]['properties'])

    if 'country' in data_location['features'][0]['properties']:
        data_country = data_location['features'][0]['properties']['country']
        data_state = data_location['features'][0]['properties']['state']
    else:
        data_country = data_location['features'][0]['properties']['address_line1']
        data_state = data_location['features'][0]['properties']['address_line2']
    # print(data_country)




    # print(iss_latitude, iss_longitude)
    print(f'{data_country}, {data_state}\nLatitude: {iss_latitude}\n'
          f'Longitude: {iss_longitude}\n')
    time.sleep(5)