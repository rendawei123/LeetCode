"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.

题意：
给一个字符串，判断它是不是回文联

解法：
两边一起进行判断，知道碰头为止
"""


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i, j = 0, len(s) - 1

        while i < j:

            while i < j and not s[i].isalnum():
                i += 1

            while j > i and not s[j].isalnum():
                j -= 1

            if s[i].lower() != s[j].lower():
                return False

            i += 1
            j -= 1

        return True

if __name__ == '__main__':
    a = Solution()
    s = 'anm,nbNm.Na'
    s1 = 'alskdf,lakds'
    s2 = ''
    print(a.isPalindrome(s2))
