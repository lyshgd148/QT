import random


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


# # 给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
# # 输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
# # 输出：6
# # 解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。
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


# 给定一个n × n的二维矩阵matrix表示一个图像。请你将图像顺时针旋转90度。你必须在原地旋转图像，
# 这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        temp = 0
        n = len(matrix)
        for i in range(n // 2):
            for j in range(n - (i + 1) * 2 + 1):
                temp = matrix[i][j + i]
                matrix[i][i + j] = matrix[n - i - j - 1][i]
                matrix[n - i - j - 1][i] = matrix[n - i - 1][n - 1 - i - j]
                matrix[n - i - 1][n - 1 - i - j] = matrix[j + i][n - i - 1]
                matrix[j + i][n - i - 1] = temp
        return matrix


martix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]


# martix= [row[::-1] for row in zip(*martix)]
# print(martix)


class Solution2(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        matrix[:] = [list(row[::-1]) for row in zip(*matrix)]
        return matrix


print(Solution2().rotate(martix))
