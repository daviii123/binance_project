import requests
from rich import print
import pandas as pd
from matplotlib import pyplot as plt
from flask import Flask

COLUMNS=['open_time',
            'open',
            'high',
            'low',
            'close',
            'volume',
            'close_time',
            'quote_asset_volume',
            'nof_trades',
            'taker_buy_base_asset_volume',
            'taker_buy_quote_asset_volume',
            'ignore'
        ]
ENDPOINT = 'https://api3.binance.com/api/v3/klines'

def get_candle(url, symbol, interval):
    params = {'symbol':symbol,'interval':interval}
    r = requests.get(url, params).json()
    return r


if __name__ == '__main__':

    response = get_candle(ENDPOINT,'BTCUSDT','15m')
    df = pd.DataFrame(response, columns=COLUMNS)
    df[['open','close']]=df[['open','close']].astype('float64')
    # df[['open','close']].iloc[0:50].plot()
    df['diff'] = df['close']/df['open']
    # df[['diff']].plot()
    # plt.show()


    app = Flask("binance")
    @app.route("/diff", methods=["GET"])
    def diff():
        dividir = df['diff'].to_json()
        return dividir


    @app.route("/inverso", methods=["GET"])
    def inverso():
        inverter = df['open'[::-1]]
        return inverter


app.run()

    
