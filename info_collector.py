from datetime import date, timedelta
import pandas as pd
from binance import Client

#We need to get both today and yesterday's date in order to get the data from Binance
today = date.today()
yesterday = today - timedelta(days=1)


dataticker = "BTCUSDT"

#We create a function to get the data from Binance and save it to a csv file
def criptodata(dataticker):
    api_key = 'Use your Api key here'
    api_secret = 'Use your Api secret here'
    client = Client(api_key, api_secret)
    prince = client.get_symbol_ticker(symbol=dataticker)
    print(prince)
    asset = dataticker
    start = "2021.01.01"
    end = str(yesterday)
    timeframe = "1d"
    df = pd.DataFrame(client.get_historical_klines(asset, timeframe, start, end))
    df = df.iloc[:, 0:6]
    df.columns = ["date", "open", "high", "low", "close", "volume"]
    df = df.set_index("date")
    df.index = pd.to_datetime(df.index, unit="ms")
    df = df.astype(float)
    print(df)
    #save to csv:
    df.to_csv(dataticker + ".csv", encoding='utf-8')

print("Data exatracted and saved to csv")
#Here you can add the crypto you want to get the data from


Crypto_list = ['BTCUSDT', "ETHUSDT", "ADAUSDT", "XRPUSDT"]
for i in Crypto_list:
    criptodata(i)
    criptodata(i)

