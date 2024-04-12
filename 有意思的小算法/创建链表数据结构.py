class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next_ = next_


ls = list(range(1, 101))


# 创建链表
def cteat_link(ls, head=None, prev=None):
    for i in range(len(ls)):
        cur = ListNode(ls[i])

        if i == 0:
            head = cur
            prev = cur
        else:
            prev.next_ = cur
            prev = cur
    return head


head = cteat_link(ls)
print(head.next_.val)
