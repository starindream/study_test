import re
from pymongo import MongoClient

__config = {
    'host': 'localhost',
    'port': 27017,
    'username': 'admin',
    'password': 'a123456'
}

# 获取连接
client = MongoClient(**__config)

# 选择数据库
db = client.test
print(db)

# 操作数据库中的某张表，并返回一个游标来保存返回的结果集。
cursor = db.student.find().sort({'age': -1})
# 操作 cursor 使用 limit 方法
cursor = cursor.limit(2)
for i in cursor:
    print('limit', i)

# MongoDB 的插入操作
result = db.py_one.insert_one({'name': '测试', 'age': 12})
print(result)
# for i in result:
#     print(i)

# 通过 explain 分析 mongodb 的查询计划。
cursor = db.student.find().explain()
print('explain', cursor)

# 使用查询条件来进行查询
range_query = {
    'age': {'$gte': 9},
}
cursor = db.student.find(range_query).skip(1).limit(1)
for i in cursor:
    print('查询', i)

# 更新文档
range_query = {
    'name': 'test'
}

cursor = db.student.update_many(range_query, {'$set': {'age': 888}})
# for i in cursor:
#     print('修改', i)

# 删除
range_query = {
    'name': {'$regex': re.compile('py')}
}

# cursor = db.student.delete_many(range_query)
cursor = db.student.find(range_query).sort({'age': -1, 'name': 1})
for i in cursor:
    print(i)

cursor = db.student.distinct('name')
for i in cursor:
    print(i)

# for i in cursor:
#     print(i)
