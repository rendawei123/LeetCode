"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note: You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2. The number of elements initialized in nums1 and nums2 are m and n respectively.

题意：
合并有序整数数组
有两个有序的整数数组nums1 和 nums2 将nums2合并到nums1中，组成一个大的有序数组
nums1有足够的空间来容纳两个数组
"""


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = []
        nums2[n:] = []
        nums1.extend(nums2)
        nums1.sort()
        return nums1

if __name__ == '__main__':
    a = [1, 2, 3]
    m = 1
    b = [4, 5]
    n = 2
    s = Solution()
    print(s.merge(a, m, b, n))
