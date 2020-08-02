import tushare as ts
import json


def connectServer():
    global json_file, pro
    with open('key.json', 'r') as json_file:
        data = json.load(json_file)
    token = data.get('token')
    return ts.pro_api(token)


def getData(freq, stkCode, startTime, endTime):
    pro = connectServer()
    # df = pro.daily(ts_code='000001.SZ', start_date='20180701', end_date='20180718')
    return pro.query(freq, ts_code=stkCode, start_date=startTime, end_date=endTime)