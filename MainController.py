import DBManager
import APIManager
import Parser


# Constant names
CNSTK = "ChinaStock"
CRYPTO = "CryptoCurrency"

# Get data thu api
rawData = APIManager.getData(CNSTK, 'daily', '000001.SZ', '20180701', '20180718')

# Parse string to json object
jsonObject = Parser.parseCNSTK(rawData)

# Save into database
error = DBManager.insert(jsonObject)
print(error)


