"""
Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.


题意：
给一个非负整数，给这个整数进行加一操作
这个非负整数表示为一个数组

注意：
首先，给这个数加一的话，数字为9的话，加一必须要进一位
如果加到最高位超出了长度的话，必须要怎加长度
"""


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

    def plusOne1(self, digits):
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
    print(a.plusOne(l2))
