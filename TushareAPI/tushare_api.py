import tushare as ts
import json


with open('../key.json', 'r') as json_file:
    data = json.load(json_file)

token = data.get('token')
pro = ts.pro_api(token)

# df = pro.daily(ts_code='000001.SZ', start_date='20180701', end_date='20180718')
df = pro.query('daily', ts_code='000001.SZ', start_date='20180701', end_date='20180718')

print(df)

json_file = "../data/000001.json"
with open(json_file, 'w') as f:
    f.write(df.to_json(orient='records', lines=True))

print("EOF")