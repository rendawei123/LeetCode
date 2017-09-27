"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example:
Input: "babad"
Output: "bab"

Note: "aba" is also a valid answer.

Example:
Input: "cbbd"
Output: "bb"

最长的回文联字符串：
从一个字符串中找出最长的回文联字符串并返回，你可以假设字符串的最大长度为1000

一般算法：
以每一个字符为中心，向两边寻找回文子串，在遍历完整个数组后，就可以找到最长的回文子串
这种算法需要考虑两种情况，一种是奇数（bob）,一种是偶数情况（moon）分别进行考虑

Manacher's Algorithm 马拉车算法


"""

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
