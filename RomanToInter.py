"""
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.

题意：
将罗马数字转化成整数
"""


class Solution(object):

    # 首先将罗马数字和整数对应的关系使用字典列出来，然后再进行循环处理
    def romanToInt(self, s):
        romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0

        if len(s) == 1:
            return romans[s]

        else:
            lists = list(s)

            for i in range(len(lists)):
                if i == len(lists)-1:
                    result += romans[lists[i]]
                    break
                if romans[lists[i]] < romans[lists[i+1]]:
                    result -= romans[lists[i]]
                else:
                    result += romans[lists[i]]
        return result


    # 简单法
    def romanToInt(self, s):
        romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0

        for i in range(0, len(s)-1):
            if romans[s[i]] < romans[s[i+1]]:
                result -= romans[s[i]]
            else:
                result += romans[s[i]]

        return result + romans[s[-1]]

if __name__ == '__main__':
    s = 'XLV'
    a = Solution()
    print(a.romanToInt(s))
