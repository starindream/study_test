import mysql.connector

config = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': 'a123456789',
    'database': 'demo'
}

try:
    conn = mysql.connector.connect(**config)
    conn.start_transaction() # 注意：开启事务必须要放到执行语句之前，即execute
    cursor = conn.cursor()
    sql = 'INSERT INTO t_emp(empno,ename,sal) VALUES(%s,%s,%s)'
    cursor.execute(sql, (9500, '赵娜', 2500))
    # conn.start_transaction()
except Exception as e:
    print(e)
finally:
    if 'conn' in dir():
        conn.close()

if __name__ == '__main__':
    pass
