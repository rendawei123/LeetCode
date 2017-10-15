"""
Implement strStr().

Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

字串匹配
返回字串在字符串中的索引，如果没有的化返回-1

解法：
由于只要求匹配出第一次出现的索引，因此只要找到就可以
直接循环一次进行匹配
"""


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for i in range(len(haystack) - len(needle)):
            if haystack[i: i + len(needle)] == needle:
                return i
            else:
                return -1

if __name__ == '__main__':
    haystack = 'aaac'
    needle = 'ac'
    a = Solution()
    print(a.strStr(haystack, needle))
