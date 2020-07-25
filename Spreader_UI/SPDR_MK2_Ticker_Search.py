import threading
import time
import pandas_datareader as web
from datetime import datetime
import datetime as dt
import pandas as pd
import asyncio

def get_yahoo_dataframe(ticker, start_date, end_date):
    # Get price data from yahoo api (deprecated api)
    price_frame = pd.DataFrame
    try:
        price_frame = web.DataReader(ticker, 'yahoo', start_date, end_date)
    except Exception:
        pass
    return price_frame

class Ticker_Scanner():
    symbols = []
    once_filtered = []

    def __init__(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.Search())

    async def Search(self):
        await asyncio.wait([self.get_symbols()]) #Get symbol list from file

        #first filter check
        first_filter_thread = threading.Thread(target=self.first_filter)
        first_filter_thread.start()




    async def get_symbols(self):
        path = 'nasdaqlisted.txt'  # ticker file
        delimiter = '|'

        with open(path, 'r') as nasdaq_list_file:
            for row in nasdaq_list_file.readlines():
                row = row.replace('\n', '')  # remove newline characters
                row_array = row.split(delimiter)
                self.symbols.append(row_array[0])

        self.symbols.pop(0) #remove the header row

    def first_filter(self):
        # static params
        start = dt.datetime(2020, 6, 1, 9, 31, 0)
        MIN_VOLUME = 7000000  # static parameters
        MIN_CLOSE = 7

        # metered loop in own thread
        for symbol in self.symbols:  # pass symbols through the first filter
            now = datetime.now()
            yh_df = get_yahoo_dataframe(symbol, start, now)

            # get the volume & close
            try:
                volume = yh_df['Volume']  # seperate relevant values
                adj_close = yh_df['Adj Close']
                last_volume = volume.tolist()[len(volume) - 1]  # get last values
                last_close = adj_close.tolist()[len(adj_close) - 1]
            except:  # incase volume is null
                last_volume = 0
                last_close = 0

            # check filter 1 conditions, above min volume, above min price
            if (last_volume >= float(MIN_VOLUME)) & (int(last_close) >= MIN_CLOSE):
                self.once_filtered.append(symbol)

                # second filter check - IV filter is triggered asynchronously
                second_filter_thread = threading.Thread(target=self.second_filter)
                second_filter_thread.start()
                print("{} - FILTER 1: PASS \n   -Volume: {:.0f}, Close: ${:.2f}".format(symbol, last_volume, last_close))
            else:
                print(symbol + " - FILTER 1: FAIL")

    def second_filter(self):
        if(len(self.once_filtered) > 0): #check for empty list
            #static params
            MIN_VOL_PCT = 50

            symbol = self.once_filtered.pop() #empty the filter


            time.sleep(5)
            print("done with level 2 task - " + symbol) #output data

#if main object, run program
if __name__ == "__main__":
    scanner = Ticker_Scanner()