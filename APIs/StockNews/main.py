import requests

STOCK = "TSLA"
COMPANY_NAME = "Tesla"

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": "UXAV96IB4GYGVN1E",
}

news_parameters = {
    "q": COMPANY_NAME,
    "apiKey": "1998a4c596364d6e982274ab6529a15a"
}

with requests.get(url="https://www.alphavantage.co/query", params=stock_parameters) as stock_response:
    stock_response.raise_for_status()
    stock_data = stock_response.json()["Time Series (Daily)"]
    days_list = []
    for item in stock_data:
        days_list.append(item)
        if len(days_list) == 2:
            break
    day_close = float(stock_data[days_list[0]]["4. close"])
    previous_day_close = float(stock_data[days_list[1]]["4. close"])
    if day_close > previous_day_close:
        percent_change = f"🔼 {round(((day_close - previous_day_close)/previous_day_close) * 100)}%"
    else:
        percent_change = f"🔽 {round(((previous_day_close - day_close)/previous_day_close) * 100)}%"
    print(percent_change)
    
with requests.get(url="https://newsapi.org/v2/top-headlines", params=news_parameters) as news_response:
    news_response.raise_for_status()
    news_data = news_response.json()["articles"]
    message = ""
    if len(news_data) == 0:
        headline = "No news for today\n"
        message += headline
    elif len(news_data) > 0:
        first_headline = f"Headline: {news_data[0]['title']}\n"
        first_brief = f"Brief: {news_data[0]['description']}\n"
        message += first_headline
        message += first_brief
        if len(news_data) > 1:
            second_headline = f"Headline: {news_data[1]['title']}\n"
            second_brief = f"Brief: {news_data[1]['description']}\n"
            message += second_headline
            message += second_brief
            if len(news_data) > 2:
                third_headline = f"Headline: {news_data[2]['title']}\n"
                third_brief = f"Brief: {news_data[2]['description']}\n"
                message += third_headline
                message += third_brief
    print(message)


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

