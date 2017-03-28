class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = '1'

        for i in range(1, n):
            s = self.count(s)

        return s

    def count(self, s):
        s1 = ''
        count = 0
        current = '#'

        for i in s:
            if i != current:
                if count != 0:
                    s1 += str(count) + str(current)
                current = i
                count = 1
            else:
                count += 1
        s1 += str(count) + str(current)

        return s1

if __name__ == '__main__':
    s = '21'
    a = Solution()
    print(a.count(s))
    n = 6
    print(a.countAndSay(n))
