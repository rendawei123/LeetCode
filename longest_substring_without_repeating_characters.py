"""
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

题目解析
在一个字符串中找到一个最长的子串，前提是子串中没有重复的字符

一、首先使用滑动窗口法，就是模拟一个滑动窗口，设置一个start，一个end，一个字典用来记录字符出现的个数，
从左到有遍历字符串，每次将end+1，然后将次数添加进字典，如果有则+1，如果没有设置为1，
每次遍历一遍之后都记录一次最大字符长度
然后判断字典里的字符个数，如果大于1，则表示有重复，start+1，否则也就是左边窗口向右滑动，这样，遍历完成之后
返回最大字符长度

二、第二种方法相比较第一种方法来说更近了一步，由于只需要求出最长的子串的长度，所以只需要一个用于跳转的指针start，和一个计数的变量maxlength即可，还需要一个用来判断是否重复的字典。
让start初次为零
遍历字符串，将第一次出现的字母以 key=s[i]:value=i 的形式存储在字典中，
每遍历一个字母，判断这个字母是否在字典中，如果不在，添加进去，如果在，说明遇到了重复字符，不符合题意，将start指针跳跃到当前循环的字符，重新开始
"""


class Solution(object):
    """
    在一个字符串中找到一个最长的子串，前提是子串中没有重复的字符,返回子串长度
    """
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 滑动窗口法

        # max_count, start, end = 0, 0, 0
        # count_dict = {}
        # for i in s:
        #     end += 1
        #     count_dict[i] = count_dict.get(i, 0) + 1
        #     while count_dict[i] > 1:
        #
        #         count_dict[s[start]] -= 1
        #         start += 1
        #     max_count = max(max_count,(end - start))
        # return max_count

        # 第二种方法，跳跃法
        max_length = start = 0
        usedChar = {}

        for i in range(len(s)):
            if s[i] in usedChar and start <= usedChar[s[i]]:
                start = usedChar[s[i]] + 1
            else:
                max_length =max(max_length, ( i - start + 1))

            usedChar[s[i]] = i
        return max_length



if __name__ == '__main__':
    s = 'pwwkew'
    s1 = 'aaaaa'
    solution = Solution()
    print(solution.lengthOfLongestSubstring(s))
