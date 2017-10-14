"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

题意：
爬楼梯，有n阶楼梯，
你可以一步走一阶或者一步走两阶最后到达最高点
问可以有多少种方法，
n为正整数

解法：
递归思想
在走最后一步的时候，分为两种情况，
    第一种情况：最后一步走一个台阶，总共的可能性为n-1的可能性
    第二种情况：最后一步走两个台阶，总共的可能性为n-2的可能性
这样问题就分解为n-1的情况和n-2的情况
终止条件为：n为2个台阶和n为1个台阶的情况，
这样递归就很好解决
"""



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
