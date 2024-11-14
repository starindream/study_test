from pymongo import MongoClient, WriteConcern
from pymongo.read_concern import ReadConcern

__config = {
    'host': 'localhost',
    'port': 27017,
    'username': 'admin',
    'password': 'a123456',
}

client = MongoClient(**__config)
db = client.test

try:
    # 注意开启会话只能通过连接来创建会话，在会话中在创建事务，一个会话中只能有一个活跃的事务
    with client.start_session() as session:
        with session.start_transaction(read_concern=ReadConcern('majority'), write_concern=WriteConcern(2)):
            db.student.insert_one({'name': 'pysix', 'age': 1}, session=session)
            session.abort_transaction()
except Exception as e:
    print('e', e)
