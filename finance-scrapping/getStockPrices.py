import requests
from bs4 import BeautifulSoup
import json
import time

# Get stock data from Yahoo Finance
# @param symbol: stock symbol
# @return: stock data


def get_data(symbol):
    headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 '}
    url = f'https://finance.yahoo.com/quote/{symbol}?p={symbol}&.tsrc=fin-srch'

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, 'html.parser')

    stock = {
        'symbol': symbol,
        'date': time.strftime("%m/%d/%Y"),
        'price': soup.find('div', {'class': "D(ib) Mend(20px)"}).find_all('fin-streamer')[0].text,
        'change': soup.find('div', {'class': "D(ib) Mend(20px)"}).find_all('fin-streamer')[1].text,
        'changePercent': soup.find('div', {'class': "D(ib) Mend(20px)"}).find_all('fin-streamer')[2].text
    }

    return stock


# Get stock data for all symbols
def get_all_data():
    symbols = ["AAPL", "AMZN", "GOOG", "FB", "TSLA", "NFLX", "MSFT", "NVDA", "JPM", "V", "MA", "BABA", "WMT", "JNJ", "XOM", "BRK-A", "BAC", "PG", "VZ", "DIS"]
    stock_data = []

    for symbol in symbols:
        stock_data.append(get_data(symbol))
        print("Stock data for " + symbol + " has been added to the list.")

    with open("stock_data.json", "w") as json_file:
        json.dump(stock_data, json_file, indent=4)
        print("Stock data has been written to stock_data.json.")

    json_file.close()
