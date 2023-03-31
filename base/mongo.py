# from pymongo import MongoClient
# import pymongo

# connection_string = "mongodb+srv://nischal:nischal@cluster0.cqtjrzl.mongodb.net/test"

# client = pymongo.MongoClient(connection_string)
# db = client['sample_medicines']


# class ProductCollection:
#     collection = db['product']

#     @classmethod
#     def create(cls, data):
#         return cls.collection.insert_one(data)

#     @classmethod
#     def read(cls, query):
#         return cls.collection.find(query)

#     @classmethod
#     def update(cls, query, data):
#         return cls.collection.update_one(query, {'$set': data})

#     @classmethod
#     def delete(cls, query):
#         return cls.collection.delete_one(query)
