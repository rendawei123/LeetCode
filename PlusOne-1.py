class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = 0

        for i in range(len(digits)):
            num += digits[i]*10**(len(digits)-i-1)

        return [int(i) for i in str(num+1)]

if __name__ == '__main__':
    l1 = [1, 2, 3, 4, 5]
    l2 = [9, 9, 9, 9, 9]
    l3 = [0]
    l4 = [1, 0, 0, 0, 0]
    a = Solution()
    print(a.plusOne(l4))
