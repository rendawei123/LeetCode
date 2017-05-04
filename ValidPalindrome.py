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

