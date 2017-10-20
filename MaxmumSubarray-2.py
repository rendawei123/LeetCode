"""
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [−2,1,−3,4,−1,2,1,−5,4],
the contiguous subarray [4,−1,2,1] has the largest sum = 6.

题意
求最大子串以及最大子串之和
"""


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        max_sum = cur_sum = nums[0]

        for each in nums[1:]:
            cur_sum = max(each, cur_sum + each)
            max_sum = max(max_sum, cur_sum)

        return max_sum

if __name__ == '__main__':
    l1 = [-9, 1, 5, -2, 7]
    a = Solution()
    print(a.maxSubArray(l1))
