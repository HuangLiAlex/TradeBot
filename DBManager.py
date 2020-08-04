from pymongo import MongoClient
import json

db = []

# Add a Document to collection
doc_1 = {"_id": 0, "name": "Alex", "age": 29}
doc_2 = {"_id": 1, "name": "Tom", "age": 25}
doc_3 = {"_id": 2, "name": "Jerry", "age": 24}
doc_4 = {"date": "2017-12-19", "open": 3266.02, "close": 3296.54, "high": 3296.94, "low": 3266.02,
         "volume": 115140134.0, "code": "sh000001"}
doc_5 = {"date": "2017-12-14", "open": 3302.93, "close": 3292.44, "high": 3309.53, "low": 3282.57,
         "volume": 120544235.0, "code": "sh000001"}


def connectDatabase(databaseName):
    # Get URL to database
    with open('key.json', 'r') as json_file:
        data = json.load(json_file)
    url = data.get('DB_URL')

    # Connect to MongoDB
    client = MongoClient(url)

    # Get the database to access
    return client[databaseName]



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
def insert(jsonObject):
    print(jsonObject)
    # Check database connection
    global db
    if not db:
        # db = connectDatabase("test")
        db = connectDatabase("TradingData")

    collection = db["SH000001"]
    
    for i in range(len(jsonObject)):
        val = jsonObject[str(i)]
        print(type(val))
        collection.insert_one(val)
    return
    
    
    # [!!!DANGEROUS ACTION!!!]
    # Delete all data for testing purpose
    #deleteCollection(collection)

    # test insert one data
    #return collection.insert_one(doc_1)


def find(collection):
    # test find one data
    return collection.find_one({"_id": 0})

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


def deleteCollection(collection):
    # [!!!DANGEROUS ACTION!!!]
    # Delete all data for testing purpose
    collection.delete_many({})

def delete():
    # [!!!DANGEROUS ACTION!!!]
    # Delete all data for testing purpose
    collection = db["SH000001"]
    collection.delete_many({})