import requests as rq


headers = {
            'Authorization': 'Bearer Z27PkjpCNc5ItQpIO2rk5k32hADHrghi'
           }

resp =  rq.get(url=\
                   'https://api.polygon.io/v2/aggs/ticker/AAPL/range/1/day/2023-01-09/2023-02-10?adjusted=true&sort=asc&apiKey=Z27PkjpCNc5ItQpIO2rk5k32hADHrghi', headers=headers)
response  = resp.raise_for_status()

data = resp.json()
print(data)
print(data['ticker'])


