from pymongo import MongoClient

url = 'mongodb+srv://sandeep:sandeep@cluster0.ea9px.mongodb.net/heraizen?authSource=admin&replicaSet=atlas-9hvn9s-shard-0&w=majority&readPreference=primary&appname=MongoDB%20Compass&retryWrites=true&ssl=true'
client = MongoClient(url)
print(client)