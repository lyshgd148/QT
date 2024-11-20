'''def MergeSort(ls):
    if len(ls)<2:
        return ls
    mid=len(ls)//2
    left,right=ls[:mid],ls[mid:]
    return merge(MergeSort(left),MergeSort(right))

def merge(left,right):
    result=[]
    while left and right:
        if left[0]<right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))
    return result


print(MergeSort([1,45,5,4,2,3,5,62,2,564,2,3]))'''


#        MergeSort()新写法

def MergeSort(ls):
    if len(ls)<2:
        return ls
    mid=len(ls)//2
    left,right=ls[:mid],ls[mid:]

    left=MergeSort(left)
    right=MergeSort(right)
    result=[]
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))
    return result

print(MergeSort([1,45,5,4,2,3,5,62,2,564,2,3]))