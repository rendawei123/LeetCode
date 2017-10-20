"""
Write a function to find the longest common prefix string amongst an array of strings.

题意：
求所有字符串的最长公共前缀，即数组的所有字符串都包含这个前缀。

解法：
合理的使用zip和set这两个内置函数，将很多迭代器的元素组成一一对应的元组，然后将元组变成集合，如果都一样的话，肯定是一个元素，然后挨个判断，如果是一个元素的话，添加到字符串中，多于一个的话，就说明是不一样的前缀，退出循环，最后的字符串就是公共前缀。
"""


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        sz, ret = zip(*strs), ''

        for each in sz:
            if len(set(each)) > 1:
                break
            ret += each[0]

        return ret

if __name__ == '__main__':
    strs1 = ['baca', 'bcba']
    strs2 = []
    strs3 = ['abc', 'adc']
    a = Solution()
    print(a.longestCommonPrefix(strs1))
    print(a.longestCommonPrefix(strs2))
    print(a.longestCommonPrefix(strs3))
