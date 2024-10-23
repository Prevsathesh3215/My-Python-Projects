import requests as rq
import datetime as dt


endpoint = 'https://pixe.la/v1/users'

USERNAME = 'prevsat321'
TOKEN = 'asdoapcnpoan[som'

params = {
    'token' : TOKEN,
    'username' : USERNAME,
    'agreeTermsOfService' : 'yes',
    'notMinor' : 'yes',

}

# resp = rq.post(url=endpoint, json=params)
# print(resp.text)

graph_endpoint = f'https://pixe.la/v1/users/{USERNAME}/graphs'

headers = {
    'X-USER-TOKEN' : TOKEN,
}

graph_config = {
    'id' : 'pixgraph',
    'name' : 'Hours Practised Programming',
    'unit' : 'hours',
    'type' : 'int',
    'color' : 'sora',

}

# resp_graph = rq.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(resp_graph.text)

pixel_endpoint = f'https://pixe.la/v1/users/{USERNAME}/graphs/pixgraph'

date_today = dt.datetime.now()
yday = date_today - dt.timedelta(1)

yday = yday.strftime('%Y%m%d')
print(yday)
date_today = date_today.strftime('%Y%m%d')

pixel_config = {
    'date' : date_today,
    'quantity' : '5',
}

# resp_pixel = rq.post(url=pixel_endpoint, json=pixel_config, headers=headers)
# print(resp_pixel.text)

pixel_put_config = {
    'quantity' : '10',
    'name' : 'Hours Practised Programming',
}


put_endpoint = f'https://pixe.la/v1/users/{USERNAME}/graphs/pixgraph/{yday}'

# resp_put = rq.put(url=put_endpoint, json=pixel_put_config, headers=headers)
# print(resp_put.text)

delete_endpoint = f'https://pixe.la/v1/users/{USERNAME}/graphs/pixgraph/{yday}'

resp_del = rq.delete(url=delete_endpoint, headers=headers)
print(resp_del.text)
