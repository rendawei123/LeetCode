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
