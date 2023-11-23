import requests, json
import pandas as pd
import yfinance

#You need to access the Yahoo Finance website and get the code in between pathentesis in
#the name of the goods you want to extract the data from (e.g. for S&P 500 the code is ^GSPC)
#The link to that one is URL = https://finance.yahoo.com/quote/%5EGSPC/

def sp500 ():
    sp500df = yfinance.Ticker("^GSPC").history(period="1y")
    sp500df.to_csv("sp500.csv", encoding='utf-8')
    print(sp500df)
    print("Extraction of S&P 500 data completed")

def gold ():
    Gold = yfinance.Ticker("GC=F").history(period="1y")
    Gold.to_csv("Gold.csv", encoding='utf-8')
    print(Gold)
    print("Extraction the data is completed")


#We need to connnect to the Forex API in order to extra the real time data.
def goldrealtime():
    Gold = json.loads(
        requests.get("https://forex-data-feed.swissquote.com/public-quotes/bboquotes/instrument/XAU/USD").text)
    data = Gold[0]
    dataclean = data['spreadProfilePrices']
    datafinish = dataclean[0]['ask']
    datafinish = str(datafinish)
    print(datafinish, end=" Gold price per Ounce ")
    print("Extraction of Gold real time data completed")
goldrealtime()


