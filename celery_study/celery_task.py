import time
import celery

"""
工作流程：
1、任务创建，celery 将创建任务并将任务信息（函数名、参数等）发送到 broker 端进行存储
2、任务分发，broker 将任务信息存入任务队列，相当于会保存当前的信息到redis中，等待worker通过连接来获取。
3、任务处理，worker 从任务队列中取出任务，执行相关的任务函数。
4、结果存储，执行结果通过 backend 存储，可供用户端进行查询。
理解：
worker 相当于程序运行中的一个守护进程，等待时间到达后，通过连接获取 broker 中存储的任务，再进行执行，然后将执行的结果再发送到 redis 进行存储。
"""

"""
知识：
1、通过 celery 实例包装后的任务，需要通过 task.delay 来进行调用，将任务交由 celery 管控，且返回结果是一个 AsyncResult 对象，可以监听结果的状态
"""

broker = 'redis://localhost:6379/9'  # redis中的 9 号逻辑库用来存储任务队列,消息代理
backend = 'redis://localhost:6379/10'  # redis中的 10 号逻辑库用来存储任务结果

# 指定name，以及 border 和 backend 的存储地址
app = celery.Celery('app')


# 通过 celery 实例 中的 task 将函数包装成一个任务,可以通过 execute.delay 来进行执行。
@app.task
def execute(name):
    print(f"向{name}发送中...")
    time.sleep(5)
    print(f'向{name}发送成功')
    return 'finally execute'
