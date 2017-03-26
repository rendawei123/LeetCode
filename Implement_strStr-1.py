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
