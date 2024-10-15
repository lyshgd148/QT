# def QuickSort(ls):
#     if len(ls)<=1:
#         return ls
#     mid=len(ls)//2
#     ls1=[]
#     ls2=[]
#     for i in range(len(ls)):
#         if i==mid:
#             continue
#         if ls[i]<=ls[mid]:
#             ls1.append(ls[i])
#         else:
#             ls2.append(ls[i])
#     mid=len(ls1)
#     ls1.append(ls[mid])
#     ls1.extend(ls2)
#     ls=ls1
#     QuickSort(ls[:mid])
#     QuickSort(ls[mid+1:])

def QuickSort(ls):
    if len(ls) <= 1:
        return ls

    mid = len(ls) // 2
    ls1 = []
    ls2 = []

    for i in range(len(ls)):
        if i == mid:
            continue
        if ls[i] <= ls[mid]:
            ls1.append(ls[i])
        else:
            ls2.append(ls[i])

    ls1 = QuickSort(ls1)
    ls2 = QuickSort(ls2)

    return ls1 + [ls[mid]] + ls2

ls=[3,4,5,7,9,8,7]
result=QuickSort(ls)
print(result)