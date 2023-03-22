import requests
import smtplib

STOCK = "TSLA"
COMPANY_NAME = "Tesla"

def get_stock():
    STOCK_API_KEY = '---'
    stock_params = {
        'function': 'TIME_SERIES_DAILY_ADJUSTED',
        'symbol': STOCK,
        'apikey': STOCK_API_KEY,
    }

    stock_res = requests.get(url='https://www.alphavantage.co/query', params=stock_params)
    stock_res.raise_for_status()
    stock_data = stock_res.json()['Time Series (Daily)']

    stock_daily_price = [float(v['4. close']) for k, v in stock_data.items()]
    ytd_closing_price = stock_daily_price[0]
    day_b4_ytd_closing_price = stock_daily_price[1]
    
    dif_close = (ytd_closing_price - day_b4_ytd_closing_price)/ytd_closing_price*100

    is_greater = False
    
    if abs(dif_close) > 5:
        is_greater = True
    
    if is_greater:
        get_news()
        send_msg(dif_close)

def get_news():
    NEWS_API_KEY= '---'

    news_params = {
        'q': COMPANY_NAME,
        'apiKey': NEWS_API_KEY,
    }

    news_res = requests.get(url='https://newsapi.org/v2/everything', params= news_params)
    news_res.raise_for_status()
    news_data = news_res.json()["articles"]
    # get top three news articles
    if len(news_data) < 3:
        n = len(news_data)
    else:
        n = 3
    
    # clear all data stored before
        with open("news.txt", 'w') as file: 
            file.write("")
            
    if n == 0:
        with open("news.txt", 'a') as file:
            file.write("So far no relevant news...")
    else:
        # input new data   
        with open("news.txt", 'a') as file:    
            news_articles = news_data[:n]
            for i in range(n):
                text = f"Title: {news_articles[i]['title']}\n" \
                    f"Author: {news_articles[i]['author']}\n" \
                    f"Description: {news_articles[i]['description']}\n" \
                    f"URL: {news_articles[i]['url']}\n\n"
                        
                file.write(text)

def send_msg(dif):
    if dif> 0:
        header = f"Subject: {STOCK}: 🔺{abs(round(dif, 1))}%"
    else:
        header = f"Subject: {STOCK}: 🔻{abs(round(dif, 1))}%"
        
    # send sms
    with open("news.txt", 'r') as file:
        text = f"{header}\n\n{file.read()}"
        text = text.encode("utf-8", "ignore")
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user='---', password='---')
            connection.sendmail(
                from_addr='---',
                to_addrs='---',
                msg=text,
            )

#----------------------------- INITIATE PROGRAM -----------------------------------#
get_stock()
