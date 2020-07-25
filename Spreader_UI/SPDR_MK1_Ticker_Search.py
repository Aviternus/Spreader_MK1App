import pandas_datareader as web
from datetime import datetime, time, timedelta
import datetime as dt
import pandas as pd
import asyncio
class Ticker_Scanner():
    def __init__(self):
        self.Search()
        pass

    def Search(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.get_symbols())
        symbols = self.get_symbols()
        once_filtered = self.first_filter(symbols)

    def first_filter(self, symbols):
        start = dt.datetime(2020, 5, 7, 9, 31, 0)
        MIN_VOLUME = 7000000  # static parameters
        MIN_CLOSE = 7
        once_filtered = []
        # Loop through every symbol and filter the dregs out
        for symbol in symbols:
            now = datetime.now()
            yh_df = self.get_yahoo_dataframe(symbol, start, now)

            # get the volume & close
            try:
                volume = yh_df['Volume']  # seperate relevant values
                adj_close = yh_df['Adj Close']
                last_volume = volume.tolist()[len(volume) - 1]  # get last values
                last_close = adj_close.tolist()[len(adj_close) - 1]
            except: #incase volume is null
                last_volume = 0
                last_close = 0

            # check filter 1 conditions, above min volume, above min price
            if (last_volume >= float(MIN_VOLUME)) & (int(last_close) >= MIN_CLOSE):
                once_filtered.append(symbol)
                print(MIN_VOLUME)
                print(last_volume)
                print("{} - FILTER 1: PASS \n   -Volume: {:.0f}, Close: ${:.2f}".format(symbol, last_volume, last_close))
            else:
                print(symbol + " - FILTER 1: FAIL")

        return once_filtered

    async def get_symbols(self):
        path = 'nasdaqlisted.txt'  # ticker file

        symbols = []
        delimiter = '|'

        with open(path, 'r') as nasdaq_list_file:
            for row in nasdaq_list_file.readlines():
                row = row.replace('\n', '')  # remove newline characters
                row_array = row.split(delimiter)
                symbols.append(row_array[0])

        symbols.pop(0) #remove the header item
        return symbols

    def get_yahoo_dataframe(self, ticker, start_date, end_date):
        # Get price data from yahoo api (deprecated api)
        price_frame = pd.DataFrame
        try:
            price_frame = web.DataReader(ticker, 'yahoo', start_date, end_date)
        except Exception:
            pass
        return price_frame

if __name__ == "__main__":
    scanner = Ticker_Scanner()