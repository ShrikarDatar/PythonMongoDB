import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["user"]

for x in mycol.find({},{ "_id": 0, "name": 1, "address": 1 }):
  print(x) 
