"""
Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

给一个整数数组，其中每个元素出现两次，只有一个元素出现一次，找到出现一次的那个元素
"""


class Solution(object):

    # 使用这种方法由于使用到了count函数，效率太低
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in nums:
            if nums.count(i) < 2:
                return i

    # 使用异或运算可以很容易的求出来
    def single_number(self, nums):
        res = 0
        for i in nums:
            res ^= i
        return res

if __name__ == '__main__':
    l = [1,1,2,2,3,3,4]
    a = Solution()
    print(a.singleNumber(l))
