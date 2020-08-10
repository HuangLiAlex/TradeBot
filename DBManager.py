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
        self.client = self.init_db()

    def init_db(self):
        with open('key.json', 'r') as json_file:
            data = json.load(json_file)
        url = data.get('DB_URL')

        # Connect to MongoDB
        return MongoClient(url)

    def get_db(self, db_name):
        # Get the database to access
        return self.client[db_name]

    def get_collection(self, collection_name, db_name):
        db = self.get_db(db_name)
        collection = db[collection_name]
        return collection

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
    def insert(self, db_name, collection_name, json_object):
        collection = self.get_collection(collection_name, db_name)

        try:
            for key, value in json_object.items():
                value["_id"] = key
                result = collection.insert_one(value)
                print(key, result)
        except Exception as ex:
            print(ex)

    # def insert_one(self, db_name, collection_name, json_object):
    #     collection = self.get_collection(collection_name, db_name)
    #     collection.insert_one(json_object)

    def find(self, db_name, collection_name):
        collection = self.get_collection(collection_name, db_name)

        find_object = collection.find({'ts_code:': collection_name})  # Find the records with ts_code
        find_object = list(find_object)  # Change to list format

        find_new_dict = {}  # Assign key value to find_object, key value = trade_date
        for i in range(len(find_object)):
            result = {find_object[i].get('trade_date'): find_object[i]}
            find_new_dict.update(result)

        find_new_dict = json.dumps(find_new_dict, default=str)
        return find_new_dict

    def find_time_range(self, db_name, collection_name, start_date, end_date):  # str
        collection = self.get_collection(collection_name, db_name)

        find_object = collection.find({
            'ts_code': collection_name,
            'trade_date': {"$gte": start_date, "$lte": end_date}
        })  # Find the records with ts_code
        find_object = list(find_object)  # Change to list format

        find_new_dict = {}  # Assign key value to find_object, key value = trade_date
        for i in range(len(find_object)):
            result = {find_object[i].get('trade_date'): find_object[i]}
            find_new_dict.update(result)

        find_new_dict = json.dumps(find_new_dict, default=str)
        # print(find_object)
        return find_new_dict


    # def delete_collection(self, collection):
    #     # [!!!DANGEROUS ACTION!!!]
    #     # Delete all data for testing purpose
    #     collection.delete_many({})

