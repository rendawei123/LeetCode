class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if not digits:
            return None

        digits.reverse()
        p = 1

        for i in range(len(digits)):
            x = digits[i] + p

            if x // 10:
                p = 1
            else:
                p = 0

            digits[i] = x % 10

        if digits[-1] == 0:
            digits.append(1)

        digits.reverse()
        return digits

if __name__ == '__main__':
    l1 = [1, 2, 3, 4, 5]
    l2 = [9, 9, 9, 9, 9]
    l3 = [0]
    l4 = [1, 0, 0, 0, 0]
    a = Solution()
    print(a.plusOne(l4))
