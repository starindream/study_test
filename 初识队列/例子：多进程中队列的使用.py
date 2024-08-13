import os
import time
import multiprocessing
 
def input_queue(q):
    info = str(os.getpid()) + '(put):' + str(time.asctime())
    q.put(info)
    print(info)
 
 
def output_queue(q):
    info = q.get()
    print('\033[32m%s\033[0m' % info)
 
 
if __name__ == '__main__':
    multiprocessing.freeze_support()
    record_one = []
    record_two = []
    queue = multiprocessing.Queue()
 
    # 放入数据
    for i in range(10):
        p = multiprocessing.Process(target=input_queue, args=(queue,))
        p.start()
        record_one.append(p)
 
    # 取出数据
    for i in range(10):
        p = multiprocessing.Process(target=output_queue, args=(queue,))
        p.start()
        record_one.append(p)
 
    for p in record_one:
        p.join()
 
    for p in record_two:
        p.join()