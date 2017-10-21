"""
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

click to show spoilers.

Have you thought about this?
Here are some good questions to ask before coding. Bonus points for you if you have already thought through this!

If the integer's last digit is 0, what should the output be? ie, cases such as 10, 100.

Did you notice that the reversed integer might overflow? Assume the input is a 32-bit integer, then the reverse of 1000000003 overflows. How should you handle such cases?

For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

Note:
The input is assumed to be a 32-bit signed integer. Your function should return 0 when the reversed integer overflows.

题意：
倒叙整数
将一个整数倒着写出来
"""


class Solution(object):

    # 这种方法就是传统方法，遍历循环判断
    def reverse(self, x):
        if type(x) == int:
            y = 0
            z = False

            if x < 0:
                z = True
                x = -x
            while True:
                if x == 0:
                    break
                else:
                    y = y * 10 + x % 10
                    x //= 10

            if -2147483648 <= y <= 2147483647:
                if z:
                    return -y
                else:
                    return y
            else:
                return 0

        else:
            return 0


    # 这种方法事先将数字大小进行判断，然后将数字转化成字符串处理，处理完后再返回
    def reverse1(self, x):
        strx = str(x)

        if x < -2147483648 or x > 2147483647:
            return 0
        elif strx[0] == '-':
            if int('-' + (strx[1:])[::-1]) >= -2147483648:
                return int('-' + (strx[1:])[::-1])
            else:
                return 0
        else:
            if int(strx[::-1]) <= 2147483647:
                return int(strx[::-1])
            else:
                return 0

if __name__ == '__main__':
    x = -123
    a = Solution()
    print(a.reverse(x))
