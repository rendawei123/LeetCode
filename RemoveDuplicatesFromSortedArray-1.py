"""
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.

题意
给定一个排序的数组，删除重复的位置，使每个元素只显示一次并返回新的长度。
不要为另一个数组分配额外的空间，您必须使用常量内存来执行此操作。

解法：
定义一个指针，指向第一个位置，遍历数组，看每一个是否和指针指向的值相等，
如果相等，判断下一个，如果不相等，指针向后移动一位
"""


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        newTail = 0
        for i in range(0, len(nums)):
            if nums[i] != nums[newTail]:
                newTail += 1
                nums[newTail] = nums[i]

        return newTail + 1


    # 依次循环，如果不相等的话删除
    def removeDuplicates1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 1

        while len(nums) > 1:
            if nums[i] == nums[i-1]:
                nums.remove(nums[i-1])
            else:
                i += 1
            if i == len(nums):
                break

        return len(nums)


if __name__ == '__main__':
    nums = []
    a = Solution()
    print(a.removeDuplicates(nums))
