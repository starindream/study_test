import time
from multiprocessing import Process, Pipe

def use_children(conn):
    time.sleep(2)
    conn.send('你好')  # 发送消息
    conn.close()       # 关闭子进程的管道连接

if __name__ == '__main__':
    parent_conn, children_conn = Pipe()
    p = Process(target=use_children, args=(children_conn,))
    p.start()
    children_conn.close() # 父进程关闭管道
    # 接收子进程发送的数据
    result = parent_conn.recv()
    print('Received:', result)
    parent_conn.recv() # 管道中没有数据，且另一端点完全被关闭，抛出EOFError错误