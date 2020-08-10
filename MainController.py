from DBManager import DBManager
import APIManager
import Parser
from datetime import date
import re

# Constant names
CNSTK = "ChinaStock"
CRYPTO = "CryptoCurrency"

# set params
today = date.today().strftime("%Y%m%d") # YYYYmmdd
stock_name = '000001.SZ'
period = 'daily'
start_time = '20200801'
end_time = today

# Get data thu api
json_object = APIManager.get_data(CNSTK, stock_name, period, start_time, end_time)

# Parse string to json object
# jsonObject = Parser.parseCNSTK(rawData)

# Save into database
database = re.sub('[ .$/\"]', '', stock_name)
dbMgr = DBManager()
error = dbMgr.insert(database, period, json_object)
print("Error: ", error)


