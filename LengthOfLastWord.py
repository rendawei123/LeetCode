"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

For example,
Given s = "Hello World",
return 5.


题意：
给一个包含大小写、空格的字符串，返回最后一个单词的长度
如果不存在，返回0
一个单词的定义是一个没有空格的字符序列
"""




class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.rstrip()
        s_list = s.split(' ')
        return len(s_list[-1])

if __name__ == '__main__':
    s1 = 'I love you ! '
    s2 = 'I '
    s3 = ''
    a = Solution()
    print(a.lengthOfLastWord(s1))
