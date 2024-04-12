class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next


ls = list(range(1, 101))


# 创建链表
def creat_link(ls, head=None, prev=None):
    for i in range(len(ls)):
        cur = ListNode(ls[i])

        if i == 0:
            head = cur
            prev = cur
        else:
            prev.next_ = cur
            prev = cur
    return head


head = creat_link(ls)
print(head.next.val)
