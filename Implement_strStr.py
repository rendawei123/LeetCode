class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle)

if __name__ == '__main__':
    haystack = 'aaac'
    needle = 'aac'
    a = Solution()
    print(a.strStr(haystack, needle))
