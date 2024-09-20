# 面向对象的好处：可以模拟现实世界的运行

from struct_ import Queue
import random


class Printer:
    def __init__(self, ppm):
        self.vec = ppm
        self.task = None
        self.time = 0

    def tick(self):
        if self.task != None:
            self.time -= 1
            if self.time <= 0:
                self.task = None

    def busy(self):
        if self.task != None:
            return True
        else:
            return False

    def newtask(self, newtask):
        self.task = newtask
        self.time = newtask.getPages() * 60 / self.vec


class Task:
    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randrange(1, 21)

    def getPages(self):
        return self.pages

    def getStamp(self):
        return self.timestamp

    def waitime(self, currenttime):
        return currenttime - self.timestamp


def newPrintask():
    num = random.randrange(1, 61)
    if num == 60:
        return True
    else:
        return False


def simulation(sec, ppm):
    printer = Printer(ppm)
    printQueue = Queue()
    waitingtime = []

    for i in range(sec):
        if newPrintask():
            task = Task(i)
            printQueue.enqueue(task)

        if (not printer.busy()) and (not printQueue.isEmpty()):
            newtask = printQueue.dequeue()
            printer.newtask(newtask)
            waitingtime.append(newtask.waitime(i))
        printer.tick()
    print(sum(waitingtime) / len(waitingtime))


for i in range(10):
    simulation(3600, 45)
