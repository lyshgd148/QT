import queue
import threading
import time

def worker(q):
    while True:
        item = q.get()  # 从队列中获取数据，如果队列为空则阻塞
        print(f"Got item from queue: {item}")
        time.sleep(1)  # 模拟处理数据的耗时操作

my_queue = queue.Queue()

# 创建并启动线程
worker_thread = threading.Thread(target=worker, args=(my_queue,))
worker_thread.start()

# 向队列中放入数据
for i in range(5):
    my_queue.put(i)
    print(f"Put item {i} into queue")
    time.sleep(1)

# 等待线程结束
worker_thread.join()

print("All items processed")