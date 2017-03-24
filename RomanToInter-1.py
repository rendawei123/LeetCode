class Solution(object):
    def romanToInt(self, s):
        romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0

        for i in range(0, len(s)-1):
            if romans[s[i]] < romans[s[i+1]]:
                result -= romans[s[i]]
            else:
                result += romans[s[i]]

        return result + romans[s[-1]]

if __name__ == '__main__':
    s = 'XLV'
    a = Solution()
    print(a.romanToInt(s))