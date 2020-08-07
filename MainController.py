from DBManager import DBManager
import APIManager
import Parser
from datetime import date

# Constant names
CNSTK = "ChinaStock"
CRYPTO = "CryptoCurrency"


today = date.today()

# YYYYmmdd
today = today.strftime("%Y%m%d")

# Get data thu api
rawData = APIManager.getData(CNSTK, 'daily', '000001.SZ', '19901219', today)

# Parse string to json object
jsonObject = Parser.parseCNSTK(rawData)

# Save into database
dbMgr = DBManager()
error = dbMgr.insert(jsonObject)
print(error)


