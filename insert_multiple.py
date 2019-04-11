import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["user"]

mylist = [
  { "name": "Ninad", "address": "Warje"},
  { "name": "Shreekar", "address": "Hadapsar"},
  { "name": "Dinesh", "address": "Wagholi"},
  { "name": "Anuj", "address": "Kothrud"},
  { "name": "Vaibhav", "address": "Sahakarnagar"},
  { "name": "Gagan", "address": "Viman Nagar"},
  { "name": "Advait", "address": "Shaniwar peth"}
]

x = mycol.insert_many(mylist)

#print list of the _id values of the inserted documents:
print(x.inserted_ids) 
