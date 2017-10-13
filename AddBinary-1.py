"""
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".

两个二进制字符串相加


"""

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if a == '0' and b == '0':   # 如果两个都是0的化，结果为零
            return '0'

        c = int(a, 2) + int(b, 2)    # 如果不是零的化，通过int('1',2)的形式将二进制转化为整数，然后相加，的到结果c
        result = ''

        while c > 0:
            result += str(c % 2)     # 将最后的结果取模，余数变成字符串，商进一位，一直循环进位再判断，余数再加进字符串
            c //= 2

        return result[::-1]   # 最后得到的字符串的方向和真实的数据是相反的，再倒过来就行了

if __name__ == '__main__':
    a = '0'
    b = '0'
    s = Solution()
    print(s.addBinary(a, b))
