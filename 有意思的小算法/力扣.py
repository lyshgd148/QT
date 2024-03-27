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


# 给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
# 输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
# 输出：6
# 解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = list()
        n = len(nums)
        temp.append(nums[0])

        for i in range(1, n):
            if temp[i - 1] > 0:
                temp.append(nums[i] + temp[i - 1])
            else:
                temp.append(nums[i])
        return max(temp)


temp = list()
for i in range(300):
    temp.append(random.randint(-15, 15))
print(temp)
print(Solution().maxSubArray(temp))
