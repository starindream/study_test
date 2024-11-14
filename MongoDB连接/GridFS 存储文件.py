from pymongo import MongoClient
from gridfs import GridFS
from bson import ObjectId

__config = {
    'host': 'localhost',
    'port': 27017,
    'username': 'admin',
    'password': 'a123456'
}

client = MongoClient(**__config)

# 获取数据库对象，该对象通过MongoClient的实例返回的。
# MongoClient内部保留着连接参数，等到操作时，可以利用这些参数进行连接
db = client.file

# 创建 FS 实例
# collection 可以指定建立表的前缀名称
fs = GridFS(db, collection='my_files')  # 传入数据库对象，指定 FS 在读写时，对指定的数据库进行读写


def write_file(path, file_name):
    # 打开文件，将文件通过 fs 模块存储进 mongoDB 中
    with open(path, 'rb') as file:
        # 将文件存储进 mongodb 文件内容会存储在数据库中的 chunk 集合中， 文件的信息存储在 files 集合中
        # 通过 files 文件中的 object_id 关联到 chunk 集合中的多个文档内容，一个文件有 chunk 集合中的多个内容拼接而成。
        add_key = {'type': 'pdf', 'my_key': 'my_value'}  # 可以通过 put 方法中传递参数，可以为存储的文件表(files文件表)中的文档内容增添自定义字段
        fs.put(file, filename=file_name, **add_key)


def read_file(file_name):
    # file_data = fs.get_last_version(filename=file_name).read()  # 获取到的是最后一次提交的相同名称的文件

    # version 表示上传相同文件的版本，0表示第一次上传的文件，1表示第二次，以此类推
    # file_data = fs.get_version(filename=file_name, version=0).read()

    # 使用 get 通过文件的 Object_id 来获取文件
    # 通过 find_one 查找文件id，find_one 查找的表是 files 的表，会返回文档信息，内部会包含更新时间等
    # file_info 默认是存储的内容，内部还具有属性可以获取到该文件的信息，通过点方法获取，可以理解为类中的property
    file_info = fs.find_one({'filename': file_name})
    file_data = fs.get(file_info._id).read()
    with open('write_test.pdf', 'wb') as file:
        # for i in file_info:
        #     file.write(i)
        file.write(file_data)


def exists_file():
    # 查找文件表（files表）中是否存在指定的信息，存在即为True
    result = fs.exists({'my_key': 'my_value'})
    print(result)


def delete_file():
    # 只能查找 files 表中的数据，查找chunks表中的字段返回的信息为 None
    filter_result = fs.find_one({'my_key': 'my_value'})
    fs.delete(filter_result._id)


if __name__ == '__main__':
    write_file(path='test.pdf', file_name='test.pdf')  # 测试传入pdf，最后能否读取
    # 测试存储两个不同的文件到 mongodb 中，名称相同的话，读取出来的文件是哪个
    # write_file(path='test_num.txt', file_name='test.txt')
    # write_file(path='test_txt.txt', file_name='test.txt')

    # 将mongodb 中的存储的文件，读取下来并创建文件夹进行存储
    # read_file('test.txt')

    # 获取 pdf 格式的文件，结果：可以完整的读取出pdf文件
    read_file(file_name='test.pdf')

    # 判断存储的文件是否存在
    # exists_file()

    # 删除mongodb中的文件，要删除files中的文件信息，以及chunks中的文件内容
    # delete_file()
