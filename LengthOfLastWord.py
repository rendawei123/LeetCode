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
