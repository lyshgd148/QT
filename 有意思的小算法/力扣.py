# 力扣:50
class Solution(object):
    def myPow(self, x, n):
        if x == 0.0:
            return 0
        res = 1

        if n < 0:
            x, n = 1 / x, -n
        while n:
            if n & 1:
                res *= x
            x *= x
            n >>= 1
        return res


print(Solution().myPow(243, 5))
