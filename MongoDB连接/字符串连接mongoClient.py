from pymongo import MongoClient

client = MongoClient("mongodb://admin:a123456@192.168.31.161:27017/admin")

data = client.test.arr.find({})

for item in data:
    print(item)

print('data', data)
