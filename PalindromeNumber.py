"""
Palindrome Number
Determine whether an integer is a palindrome. Do this without extra space.

题意：
判断一个整数列是否是回文联，不需要额外空间

反转比较法 Reverse and Compare
复杂度
时间 O(n) 空间 O(1)

思路
回文数有一个特性，就是它反转后值是一样的。所以我们可以先将其反转，然后比较反转数和原数是否相等。该方法的问题在于溢出的判断和处理，我们可以参考反转整数中的几种处理方法。

逐位比较法 One By One
复杂度
时间 O(n) 空间 O(1)

思路
反转比较有可能会溢出，但我们遍历每一位的时候其实并不用保存上一位的信息，只要和当前对应位相等就行了。所以我们可以遍历一遍先算出数的长度，再遍历一遍同时对比前后的对应位。

本题采用反转比较法
"""

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
