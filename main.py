import requests
import datetime as dt

from SmsMechanism import smsMachine

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = "Y24LYCZUZ0OA300C"
NEWS_API_KEY = "fd50e030636c4121bc6d4ea6e9974751"
# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
parameter = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY
}
stock_Url = "https://www.alphavantage.co/query"

response = requests.get(url=stock_Url, params=parameter)
response.raise_for_status()

dateWise = response.json()["Time Series (Daily)"]
dataList = [value for (key, value) in dateWise.items()]

yesterday_price = dataList[0]["4. close"]
before_yesterday_price = dataList[1]["4. close"]
# print(yesterday_price, before_yesterday_price)

diff_percentage = round(((float(yesterday_price) - float(before_yesterday_price)) / float(yesterday_price)) * 100)
updown = ""
if diff_percentage > 0:
    updown = "🔺"
else:
    updown = "🔻"
# print(diff_percentage)

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
Newsparameter = {
    "q": COMPANY_NAME,
    "apiKey": NEWS_API_KEY,
}
news_Url = "https://newsapi.org/v2/everything"

response = requests.get(url=news_Url, params=Newsparameter)
response.raise_for_status()

allDataTesla = response.json()
articles = allDataTesla["articles"][:3]

formatedSMS = [f"{STOCK}: {updown}{diff_percentage}%\nHeadline: {article['title']}.\nBrief: {article['description']}."
               for article in articles]

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 

if abs(diff_percentage) > 5:
    for msg_body in formatedSMS:
        smsMachine(msg_body)
else:
    print("Sotck not diffrence too mach!")

