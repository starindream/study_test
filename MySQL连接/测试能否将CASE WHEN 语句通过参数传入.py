import mysql.connector.pooling as pooling

config = {
    'host':'localhost',
    'port':3306,
    'user':'root',
    'password':'a123456789',
    'database':'demo'
}

try:
    pool = pooling.MySQLConnectionPool(**config,pool_size=5)
    conn = pool.get_connection()
    conn.start_transaction()
    cursor = conn.cursor()
    # 结论：不能进行运行，因为SQL中的参数中只能传入字符格式，不能传入SQL逻辑部分。
    case_when = 'CASE deptno WHEN 30 THEN "SALES" WHEN 20 THEN "RESEARCH" ELSE "未知" END'
    sql = 'SELECT %s FROM t_emp'
    cursor.execute(sql)
except Exception as e:
    if 'conn' in dir():
        conn.rollback()
    print(e)

if __name__ == '__main__':
    pass