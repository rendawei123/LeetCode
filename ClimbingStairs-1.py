class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        ways = [1, 2]

        for i in range(2, n):
            ways.append(0)
            ways[i] = ways[i - 1] + ways[i - 2]

        return ways[n-1]

if __name__ == '__main__':
    n = 5
    s = Solution()
    print(s.climbStairs(n))
