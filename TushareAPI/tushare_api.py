import tushare as ts
import json
import time


def connectServer():
    global json_file, pro
    with open('key.json', 'r') as json_file:
        data = json.load(json_file)
    token = data.get('token')
    return ts.pro_api(token)


# def getData(freq, stkCode, startTime, endTime):
#     pro = connectServer()
#     # df = pro.daily(ts_code='000001.SZ', start_date='20180701', end_date='20180718')
#     return pro.query(freq, ts_code=stkCode, start_date=startTime, end_date=endTime)


def getData(freq, stkCode, startDate, endDate):
    pro = connectServer()
    df = pro.trade_cal(exchange='SSE', is_open='1',
                       start_date=startDate,
                       end_date=endDate,
                       fields='cal_date')

    for date in df['cal_date'].values:
        df = get_daily(stkCode, date)

    return df


def get_daily(ts_code='', trade_date='', start_date='', end_date=''):
    pro = connectServer()
    for _ in range(3):
        try:
            if trade_date:
                print(trade_date)
                df = pro.daily(ts_code=ts_code, trade_date=trade_date)
                print(df)
            else:
                df = pro.daily(ts_code=ts_code, start_date=start_date, end_date=end_date)
        except Exception as e:
            print(e)
            time.sleep(1)
        else:
            return df
