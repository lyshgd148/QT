#冒泡排序法(从小到大)
def sort_list_small(list_):
    n=len(list_)
    for i in range(n-1):
        for j in range(n-1-i):
            if list_[j+1]<=list_[j]:
                list_[j+1],list_[j]=list_[j],list_[j+1]
