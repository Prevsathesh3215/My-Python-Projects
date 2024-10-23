STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

import requests as rq
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

EQUITY = 'TSLA'


def get_stocks():
    resp = rq.get(url=f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={EQUITY}&apikey=CCDNYKD9O4ZV64CU')
    data = resp.json()
    # print(data)

    days = list(data['Time Series (Daily)'])
    dates = days.copy()

    for i in range(len(days)):
        days[i] = float(data['Time Series (Daily)'][days[i]]['4. close'])

    # for i in range(0, len(days) - 1):
    #     diff = ((days[i] - days[i+1]) / days[i]) * 100
    #
    #     if diff > 5:
    #         print(f'TSLA: 🔺{round(diff, 2)}%, at {dates[i]}')
    #         get_news()
    #
    #     elif diff < -5:
    #         print(f'TSLA: 🔻{round(diff, 2)} %, at {dates[i]}')
    #         get_news()

    fig, ax = plt.subplots()

    ax.plot(dates, days, 'x',  markeredgewidth=2)
    plt.show()




def get_news():
    resp_news = rq.get(url='https://newsapi.org/v2/everything?q=tesla&from=2024-08-15&sortBy=publishedAt&apiKey=1ee414ff4d7f4bb7bda8309b62e559ee')
    news_data = resp_news.json()
    # print(news_data)

    # print(news_data['articles'][0])




    # for articles in news_data['articles']:
    #     print(articles)
    #     if articles['publishedAt'][0:10] == date:
    #         news.append([articles['title'], articles['url']])
    #
    # print(news)



    news = [[news_data['articles'][i]['title'], news_data['articles'][i]['url']] for i in range(0, 3)]

    for x in news:
        print(f'\nHeadline:{x[0]}')
        print(f'URL:{x[1]}')



get_stocks()


# print(type(str(yesterday)))
# print(round(diff, 2), '%')
