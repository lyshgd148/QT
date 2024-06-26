import matplotlib.pyplot as plt

with open('Set.txt', 'r') as f:
    set = f.read()
    set = int(set)

with open('UART.txt', 'r') as f:
    content = f.read()
    content = content.split(' ')
    while ' ' in content:
        content.remove(' ')

vel = list()
time = list()
for i in range(len(content)):
    if i % 2 == 0:
        vel.append(int(content[i]))
    else:
        time.append(int(content[i]))


def process_VT(vel, tim):
    global time
    temp = list()
    m = len(vel)
    n = len(tim)
    if m > n:
        m -= 1
        vel.pop(-1)
    elif m < n:
        n -= 1
        tim.pop(-1)
    for i in range(n):
        temp.append(sum(tim[0:i + 1]) / 100)
    time = temp


process_VT(vel, time)
Set = [set for _ in range(len(time))]

plt.plot(time, vel, color='black', label='Velocity')
plt.plot(time, Set, color='r', label='Set')
plt.title('PID-Modify')
plt.xlabel('time(s)')
plt.ylabel('Velocity()')
plt.legend()
plt.show()
