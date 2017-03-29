class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if a == '0' and b == '0':
            return '0'

        c = int(a, 2) + int(b, 2)
        result = ''

        while c > 0:
            result += str(c % 2)
            c //= 2

        return result[::-1]

if __name__ == '__main__':
    a = '0'
    b = '0'
    s = Solution()
    print(s.addBinary(a, b))