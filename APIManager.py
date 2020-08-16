from TushareAPI import tushare_api
from BinanceAPI import binance_api


def get_data(category, stk_code, freq, start_time, end_time, q):
    if category == "ChinaStock":
        tushare_api.get_data(stk_code, freq, start_time, end_time, q)
    if category == "CryptoCurrency":
        binance_api.get_data()


