from pymongo import MongoClient
import json


class DBManager:
    def __init__(self):
        self.client = self._init_db()

    def _init_db(self):
        with open('key.json', 'r') as json_file:
            data = json.load(json_file)
        url = data.get('DB_URL')

        # Connect to MongoDB
        return MongoClient(url)

    def _get_db(self, db_name):
        # Get the database to access
        return self.client[db_name]

    def _get_collection(self, collection_name, db_name):
        db = self._get_db(db_name)
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
        collection = self._get_collection(collection_name, db_name)

        for key, value in json_object.items():
            try:
                value["_id"] = key
                result = collection.insert_one(value)
                print(key, result)
            except Exception as ex:
                print(ex)

    def find(self, db_name, collection_name):
        try:
            collection = self._get_collection(collection_name, db_name)

            find_object = collection.find({})  # Find the records with ts_code
            find_object = list(find_object)  # Change to list format

            find_new_dict = {}  # Assign key value to find_object, key value = trade_date
            for i in range(len(find_object)):
                result = {find_object[i].get('trade_date'): find_object[i]}
                find_new_dict.update(result)

            find_new_dict = json.dumps(find_new_dict, default=str)
            return False, find_new_dict

        except Exception as ex:
            return True, ex

    def find_time_range(self, db_name, collection_name, start_date, end_date):  # str
        collection = self._get_collection(collection_name, db_name)

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

