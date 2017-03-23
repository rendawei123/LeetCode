class Solution(object):
    def isPalindrome(self, x):
        strx = str(x)
        if strx == strx[::-1]:
            return True
        else:
            return False

if __name__ == '__main__':
    x = 0
    a = Solution()
    print(a.isPalindrome(x))