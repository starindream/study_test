import mysql.connector

db = mysql.connector.connect(host="localhost", user="root", password="a123456789", database="demo")

cursor = db.cursor()

sql = 'SELECT * FROM t_emp'
cursor.execute(sql)

cursor2 = db.cursor()
cursor2.execute(sql)




# 插入多条信息


# values = (9920, 'test_insert')
# cursor.execute("DELETE FROM t_emp WHERE empno=9090")

# cursor.execute('SELECT * FROM t_emp WHERE empno>8000')
#
# print('cursor',cursor)
#
# for i in cursor:
#     print(i)
#
#
# result_one = cursor.fetchone()
# print('result_one', result_one)

# cursor.close()
# print('连接成功')
# db.commit()

if __name__ == '__main__':
    print(db)
