#Description
This tool helps in getting trading data (Klines) using different APIs, and save it into MongoDB Altas. 
End User can fetch data from MongoDB Altas.

#Usage 
##API call
find all history for one stock
##Input 
1. stock code. eg. SH000001
1. period: weekly, daily, 1_hour, 15_min, 5_min, 1_min.

```python
from DBManager import DBManager
dbMgr = DBManager()
error = dbMgr.find(trade_code, period)
```

##Output
A Json object contains several lines of small Json records
Each Json record is a "trade_date" : Json object pair
```json
{
	"20180718": {
		"ts_code": "000001.SZ",
		"trade_date": "20180718",
		"open": 8.75,
		"high": 8.85,
		"low": 8.69,
		"close": 8.7,
		"pre_close": 8.72,
		"change": -0.02,
		"pct_chg": -0.23,
		"vol": 525152.77,
		"amount": 460697.377
	},
	"20180717": {
		"ts_code": "000001.SZ",
		"trade_date": "20180717",
		"open": 8.74,
		"high": 8.75,
		"low": 8.66,
		"close": 8.72,
		"pre_close": 8.73,
		"change": -0.01,
		"pct_chg": -0.11,
		"vol": 375356.33,
		"amount": 326396.994
	}
}
```
#Progress
- [x] API module
    - [x] Tushare API
        - [x] Daily klines
        - [ ] Other periods
    - [x] Binance API
        - [x] Daily klines
        - [ ] Other periods
- [x] Database module
    - [x] insert
    - [x] insert_one
    - [x] find
    - [x] find with dates
    - [ ] RFU
- [x] Parser module
- [x] Control unit 