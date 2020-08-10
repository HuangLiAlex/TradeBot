from TushareAPI import tushare_api
from BinanceAPI import binance_api


def get_data(category, stk_code, freq, start_time, end_time):
    data = []
    if category == "ChinaStock":
        data = tushare_api.get_data(stk_code, freq, start_time, end_time)
    if category == "CryptoCurrency":
        data = binance_api.get_data()

    if len(data) > 0:
        return data
    else:
        return False

