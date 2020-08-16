import tushare as ts
import json
import time

json_file = ''
pro = []


def connect_server():
    global json_file, pro
    with open('key.json', 'r') as json_file:
        data = json.load(json_file)
    token = data.get('token')
    pro = ts.pro_api(token)
    if pro:
        print("Connected to tushare api server.")
    return pro


# def getData(freq, stkCode, startTime, endTime):
#     pro = connectServer()
#     # df = pro.daily(ts_code='000001.SZ', start_date='20180701', end_date='20180718')
#     return pro.query(freq, ts_code=stkCode, start_date=startTime, end_date=endTime)


def get_data(stk_code, freq, start_time, end_time, q):
    global pro
    if not pro:
        connect_server()

    # step 1: get trade calendar
    df = pro.trade_cal(exchange='SSE', is_open='1',
                       start_date=start_time,
                       end_date=end_time,
                       fields='cal_date')

    # step 2: fetch daily data
    for date in df['cal_date'].values:
        df = get_daily(stk_code, date)
        if df.empty:
            print(date, "fail")
            pass
        else:
            print(date, "get")
            value = json.loads(df.to_json(orient='records', lines=True))
            data = {date: value}
            q.put(data)


def get_daily(ts_code='', trade_date='', start_date='', end_date=''):
    global pro
    if not pro:
        connect_server()

    for _ in range(3):
        try:
            if trade_date:
                df = pro.daily(ts_code=ts_code, trade_date=trade_date)
            else:
                df = pro.daily(ts_code=ts_code, start_date=start_date, end_date=end_date)
        except Exception as e:
            print(e)
            time.sleep(1)
        else:
            return df
