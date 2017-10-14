"""
采用普通递归的方法，但是这种方法，如果递归很多层，效率很低，时间复杂度很高
"""

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs(n-1) + self.climbStairs(n-2)

if __name__ == '__main__':
    n = 5
    s = Solution()
    print(s.climbStairs(n))
