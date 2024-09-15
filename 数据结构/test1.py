import threading


def compute():
    for _ in range(1000000):
        pass


threads = []
for _ in range(1000):
    thread = threading.Thread(target=compute)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

code_block = """
code='''
import threading


def compute():
    for i in range(1000000):
        pass


threads = []
for _ in range(1000):
    thread = threading.Thread(target=compute)
    thread.start()
    threads.append(thread)


for thread in threads:
    thread.join()

'''
import threading


def compute():
    for _ in range(1000000):
        pass


threads = []
for _ in range(1000):
    thread = threading.Thread(target=compute)
    thread.start()
    threads.append(thread)


for thread in threads:
    thread.join()
exec(code)
"""
exec(code_block)
