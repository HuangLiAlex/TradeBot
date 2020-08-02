from TushareAPI import tushare_api
from BinanceAPI import binance_api


def getData(category, freq, stkCode, startTime, endTime):
    data = []
    if category == "ChinaStock":
        data = tushare_api.getData(freq, stkCode, startTime, endTime)
    if category == "CryptoCurrency":
        data = binance_api.getData()

    if data.size > 0:
        return data
    else:
        return False

