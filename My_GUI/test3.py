import threading
import time
import queue

# 定义一个函数作为线程的执行体
def print_numbers(q):
    for i in range(1, 6):
        q.put(f"Number: {i}")
        time.sleep(1)

# 创建一个队列用于线程间通信
q = queue.Queue()

# 创建线程，传入队列作为参数
thread = threading.Thread(target=print_numbers, args=(q,))

# 启动线程
thread.start()

# 主线程从队列中获取数据并打印
while not q.empty():
    print(q.get())

# 主线程继续执行其他任务
for i in range(1, 4):
    print(f"Main thread: {i}")
    time.sleep(1)

while not q.empty():
    print(q.get())
# 等待子线程执行完毕
thread.join()

print("Main thread and child thread have finished.")