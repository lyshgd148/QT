import subprocess
import threading

# NB的方法 如果要运行的文件里面有堵塞 例如：while循环 考虑开多线程来运行。哈哈哈哈！
file_path = r"./辛普森积分.py"


def run():
    subprocess.run(["python", file_path])


threads = list()
for _ in range(10):
    t = threading.Thread(target=run)
    threads.append(t)

for t in threads:
    t.start()
