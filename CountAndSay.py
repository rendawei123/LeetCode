"""
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

Example 1:

Input: 1
Output: "1"
Example 2:

Input: 4
Output: "1211"


题意：
    数数字然后说出来，说的都是上一个的内容
    1
    11   前一个数读为一个一，
    21   前一个数读为两个一
    1211 前一个数读为一个二，一个一
    ...依次类推

    求第n个数为多少？

解法：
    首先求出上一个数每一次说出来的值，
    然后求第n个数的总值

"""



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
