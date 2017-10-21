"""
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0

给一个有序数组和一个目标值，如果数组里面有目标值的话，返回其索引，如果没有的目标值的话，假设将目标值插入有序数组中，返回目标值的索引
"""


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums:
            i = 0
            while nums[i] < target:
                i += 1
                if i == len(nums):
                    break
            return i
        return 0

    def searchInsert1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return len([x for x in nums if x<target])

if __name__ == '__main__':
    nums = [1]
    target = 0
    a = Solution()
    print(a.searchInsert(nums, target))
