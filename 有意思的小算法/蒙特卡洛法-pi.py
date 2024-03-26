import random
def my_Pi(n):
    hits=0
    for i in range(n):
        x=random.random()*2-1
        y=random.random()*2-1
        if x**2+y**2<=1:
            hits+=1
    return 4*(hits/n)
my_Pi(10000000)
