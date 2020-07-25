# Import the client
from td.client import TDClient

symbol = 'MSFT'

class C_Spread:
    def __init__(self):
        # Login to the session
        session = self.get_TDClient()
        session.login()

        # Grab real-time quotes for 'MSFT' (Microsoft)
        instrument = session.get_quotes(instruments=[symbol])
        volume = instrument[symbol]['totalVolume']
        last_price = instrument[symbol]['lastPrice']

        print(instrument)
        print(volume)
        print(last_price)

    def get_TDClient(self):
        # Create a new session, credentials path is optional.
        TDSession = TDClient(
            client_id='LZGUB1XDODQPG9D95BZ0G7ZV8AMAUVM8',
            redirect_uri="http://localhost/green_chip",
            credentials_path="credentials.json"
        )
        return TDSession

    def get_symbols(self):
        path = 'nasdaqlisted.txt'  # ticker file
        delimiter = '|'

        with open(path, 'r') as nasdaq_list_file:
            for row in nasdaq_list_file.readlines():
                row = row.replace('\n', '')  # remove newline characters
                row_array = row.split(delimiter)
                self.symbols.append(row_array[0])

        self.symbols.pop(0)  # remove the header row

if __name__ == "__main__":
    c_spread = C_Spread()