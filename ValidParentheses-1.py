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