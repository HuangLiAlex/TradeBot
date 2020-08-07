from pymongo import MongoClient
import json


# Add a Document to collection
doc_1 = {"_id": 0, "name": "Alex", "age": 29}
doc_2 = {"_id": 1, "name": "Tom", "age": 25}
doc_3 = {"_id": 2, "name": "Jerry", "age": 24}
doc_4 = {"date": "2017-12-19", "open": 3266.02, "close": 3296.54, "high": 3296.94, "low": 3266.02,
         "volume": 115140134.0, "code": "sh000001"}
doc_5 = {"date": "2017-12-14", "open": 3302.93, "close": 3292.44, "high": 3309.53, "low": 3282.57,
         "volume": 120544235.0, "code": "sh000001"}


class DBManager:
    def __init__(self):
        self.client = self.initDB()

    def initDB(self):
        with open('key.json', 'r') as json_file:
            data = json.load(json_file)
        url = data.get('DB_URL')

        # Connect to MongoDB
        return MongoClient(url)

    def getDB(self, databaseName):
        # Get the database to access
        return self.client[databaseName]

    """
    # Input: a Json object contains several Json objects
    # { 
    #   {key:value, key:value, ...}, 
    #   {key:value, key:value, ...}, 
    #   ...
    # }
    #
    # Output: boolean: True or False
    """
    def insert(self, jsonObject):
        db = self.getDB("TradingData") # TBD: db name change to stock code. eg.SH000001
        collection = db["SH000001"] # TBD: change collecton name to period. eg.daily, weekly, monthly

        for i in range(len(jsonObject)):
            val = jsonObject[str(i)]
            collection.insert_one(val)
        return
    
    def insert_One(self, jsonObject):
        db = self.getDB("TradingData") # TBD: db name change to stock code. eg.SH000001
        collection = db["SH000001"] # TBD: change collecton name to period. eg.daily, weekly, monthly

        collection.insert_one(jsonObject)
        return

    def find(self, code):
        db = self.getDB('TradingData')
        collection = db['SH000001']
        
        find_object = collection.find({'ts_code': code}) # Find the records with ts_code
        find_object = list(find_object) # Change to list format
        
        find_NewDict = {} # Assign key value to find_object, key value = trade_date
        for i in range(len(find_object)):
            Dict = {find_object[i].get('trade_date'): find_object[i]}
            find_NewDict.update(Dict)
        
        find_NewDict = json.dumps(find_NewDict, default = str)
        #print(find_object)
        return find_NewDict
        #return collection.find_one({"_id": 0})

        # # Insert multiple data
        # collection.insert_many([doc_2, doc_3])
        # # Find all data
        # result = collection.find({})
        # print('Find all data: ')
        # for user in result:
        #     print(user)
        #
        # # Update data
        # collection.update_one({"_id":0}, {"$set": {"age": 31, "category": "human"}})
        # # Find one data
        # result = collection.find_one({"_id":0})
        # print('Find one data: ', result)
        #
        # # Insert one data
        # collection.insert_one(doc_4)
        # collection.insert_one(doc_5)
        # # Find one data
        # result = collection.find({"date":"2017-12-19"})
        # print('Find all data: ')
        # for keyValue in result:
        #     print(keyValue)
    
    def find_TimeRange(self, code, start_date, end_date): # str
        db = self.getDB('TradingData')
        collection = db['SH000001']
        
        find_object = collection.find({
                                        'ts_code': code,
                                        'trade_date': {"$gte": start_date, "$lte": end_date}
                                        }) # Find the records with ts_code
        find_object = list(find_object) # Change to list format
        
        find_NewDict = {} # Assign key value to find_object, key value = trade_date
        for i in range(len(find_object)):
             Dict = {find_object[i].get('trade_date'): find_object[i]}
             find_NewDict.update(Dict)
        
        find_NewDict = json.dumps(find_NewDict, default = str)
        # #print(find_object)
        return find_NewDict


    def deleteCollection(self, collection):
        # [!!!DANGEROUS ACTION!!!]
        # Delete all data for testing purpose
        collection.delete_many({})

def delete():
    # [!!!DANGEROUS ACTION!!!]
    # Delete all data for testing purpose
    collection = db["SH000001"]
    collection.delete_many({})