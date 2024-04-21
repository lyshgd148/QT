import random
import time

# # 力扣:50
# class Solution(object):
#     def myPow(self, x, n):
#         if x == 0.0:
#             return 0
#         res = 1
#
#         if n < 0:
#             x, n = 1 / x, -n
#         while n:
#             if n & 1:
#                 res *= x
#             x *= x
#             n >>= 1
#         return res
#
#
# print(Solution().myPow(243, 5))


# 力扣53
# class Solution(object):
#     def maxSubArray(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         temp = list()
#         n = len(nums)
#         temp.append(nums[0])
#
#         for i in range(1, n):
#             if temp[i - 1] > 0:
#                 temp.append(nums[i] + temp[i - 1])
#             else:
#                 temp.append(nums[i])
#         return max(temp)
#
#
# temp = list()
# for i in range(300):
#     temp.append(random.randint(-15, 15))
# print(temp)
# print(Solution().maxSubArray(temp))


# # 力扣48
# class Solution(object):
#     def rotate(self, matrix):
#         """
#         :type matrix: List[List[int]]
#         :rtype: None Do not return anything, modify matrix in-place instead.
#         """
#         temp = 0
#         n = len(matrix)
#         for i in range(n // 2):
#             for j in range(n - (i + 1) * 2 + 1):
#                 temp = matrix[i][j + i]
#                 matrix[i][i + j] = matrix[n - i - j - 1][i]
#                 matrix[n - i - j - 1][i] = matrix[n - i - 1][n - 1 - i - j]
#                 matrix[n - i - 1][n - 1 - i - j] = matrix[j + i][n - i - 1]
#                 matrix[j + i][n - i - 1] = temp
#         return matrix
#
#
# class Solution2(object):
#     def rotate(self, matrix):
#         """
#         :type matrix: List[List[int]]
#         :rtype: None Do not return anything, modify matrix in-place instead.
#         """
#         matrix[:] = [list(row[::-1]) for row in zip(*matrix)]
#         return matrix
#
#
# martix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
# print(Solution2().rotate(martix))


# # 模拟链表
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
#
# def creat_link(ls, head=None, prev=None):
#     for i in range(len(ls)):
#         cur = ListNode(ls[i])
#
#         if i == 0:
#             head = cur
#             prev = cur
#         else:
#             prev.next = cur
#             prev = cur
#     return head
#
#
# ls = [1, 2, 3, 4, 5]
# head = creat_link(ls)
#
#
# class Solution(object):
#     def rotateRight(self, head, k):
#         if not head:
#             return head
#         n = 1
#         cur = head
#
#         while cur.next:
#             cur = cur.next
#             n += 1
#
#         cur.next = head
#
#         if (sum := n - k % n) == n:
#             return head
#
#         while sum :
#             cur = cur.next
#             sum -= 1
#
#         ret = cur.next
#         cur.next=None
#         return ret
#
# start=Solution().rotateRight(head,2)
# while start.next:
#     print(start.val)
#     start=start.next


# 63
start = time.time()


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        num = 0

        def dfs(i, j):
            nonlocal num
            if i > m - 1 or j > n - 1 or obstacleGrid[i][j] == 1:
                return
            if i == m - 1 and j == n - 1:
                num += 1
                return

            dfs(i + 1, j)
            dfs(i, j + 1)

        dfs(0, 0)
        return num


temp = [[0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0],
        [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1],
        [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
        [1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
        [0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0],
        [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0],
        [1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
        [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]]

num = Solution().uniquePathsWithObstacles(temp)
end = time.time()
# print(len(temp),len(temp[0])) #29行 18列
print(f'时间{end - start},路径{num}') #时间30.842482089996338,路径13594824  (这个计算出结果的时间肯定是不行的呀！！！)
