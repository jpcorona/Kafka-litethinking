from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client['kafka_db']
collection = db['messages']

for message in consumer:
    collection.insert_one(message.value)
