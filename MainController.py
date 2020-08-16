from DBManager import DBManager
from datetime import date
from queue import Queue
import APIManager
import threading
import re

# Constant names
CNSTK = "ChinaStock"
CRYPTO = "CryptoCurrency"
exit_flag = False


def fetch_data(param, q):
    global exit_flag
    # Get data thu api
    APIManager.get_data(
        param['stock_type'],
        param['stock_name'],
        param['period'],
        param['start_time'],
        param['end_time'],
        q
    )
    exit_flag = True


def store_data(param, q):
    global exit_flag
    db_mgr = DBManager()

    while not q.empty() or not exit_flag:
        if not q.empty():
            data = q.get()
            database = re.sub('[ .$/\"]', '', param['stock_name'])
            db_mgr.insert(database, param['period'], data)


def multithreading(param):
    global exit_flag
    q = Queue()
    threads = []
    exit_flag = False

    t_fetch = threading.Thread(name='fetch data', target=fetch_data, args=(param, q))
    t_fetch.start()
    threads.append(t_fetch)

    t_store = threading.Thread(name='store data', target=store_data, args=(param, q))
    t_store.start()
    threads.append(t_store)

    for t in threads:
        t.join()

    print('task complete')


if __name__ == '__main__':
    start_date_SZ000001 = '19901231'
    today = date.today().strftime("%Y%m%d")  # YYYYmmdd
    param = {
        'stock_type': CNSTK,
        'stock_name': '000001.SZ',
        'period': 'daily',
        'start_time': start_date_SZ000001, 
        'end_time': today
    }

    multithreading(param)
