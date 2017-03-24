class Solution(object):
    def romanToInt(self, s):
        romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0

        if len(s) == 1:
            return romans[s]

        else:
            lists = list(s)

            for i in range(len(lists)):
                if i == len(lists)-1:
                    result += romans[lists[i]]
                    break
                if romans[lists[i]] < romans[lists[i+1]]:
                    result -= romans[lists[i]]
                else:
                    result += romans[lists[i]]
        return result

if __name__ == '__main__':
    s = 'XLV'
    a = Solution()
    print(a.romanToInt(s))
