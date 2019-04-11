import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["users"]

mydict = { "name": "Ninad", "address": "Pune" }

x = mycol.insert_one(mydict)
