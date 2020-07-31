from pymongo import MongoClient


# Connect to Mongo
client = MongoClient("mongodb+srv://huangli:huangli123456@tradebotcluster.czq2u.mongodb.net/test?retryWrites=true&w=majority")

# Get the database you want to access
db = client["test"]
collection = db["test"]

# [!!!DANGEROUS ACTION!!!]
# Delete all data for testing purpose
collection.delete_many({})

# Add a Document to collection
doc_1 = {"_id":0, "name": "Alex", "age": 30}
doc_2 = {"_id":1, "name": "Tom", "age": 25}
doc_3 = {"_id":2, "name": "Jerry", "age": 24}

# Insert one data
collection.insert_one(doc_1)
# Find one data
result = collection.find_one({"_id":0})
print('Find one data: ', result)

# Insert multiple data
collection.insert_many([doc_2, doc_3])
# Find all data
result = collection.find({})
print('Find all data: ')
for user in result:
    print(user)

# Update data
collection.update_one({"_id":0}, {"$set": {"age": 31, "category": "human"}})
# Find one data
result = collection.find_one({"_id":0})
print('Find one data: ', result)



