"""
Implement int sqrt(int x).

Compute and return the square root of x.

实现函数int sqrt(int x)
"""


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        result = x

        while result ** 2 - x > 0:
            result = (result + x / result) / 2

        return result

if __name__ == '__main__':
    x = 4
    a = Solution()
    print(a.mySqrt(x))
