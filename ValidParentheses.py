"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

题意：
括号匹配问题
"""


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        parentheses = {')': '(', ']': '[', '}': '{'}
        s_parentheses = []
        result = True
        for each in s:
            if each in parentheses.values():
                s_parentheses.append(each)

            else:
                if s_parentheses:
                    if parentheses[each] != s_parentheses.pop():
                        result = False
                        break

                else:
                    result = False

        if s_parentheses:
            result = False

        return result

if __name__ == '__main__':
    s = '['
    a = Solution()
    print(a.isValid(s))
