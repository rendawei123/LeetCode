"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note: You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2. The number of elements initialized in nums1 and nums2 are m and n respectively.

题意：
合并有序整数数组
有两个有序的整数数组nums1 和 nums2 将nums2合并到nums1中，组成一个大的有序数组
nums1有足够的空间来容纳两个数组

解法：倒序存储
复杂度
时间 O(N+M) 空间 O(1)

思路
提示第一个数组的大小足以装两个数组，所以自然想到把两个数组都合并到第一个数组中，但是第一个数组前面都是有用的信息，如果直接从前面加，我们得将后面所有的数都位移。但是如果我们从后往前，合并到第一个数组的最后，则不用位移。
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
        while m > 0 and n > 0:
            if nums1[m - 1] >= nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
        if n > 0:
            nums1[:n] = nums2[:n]

        return nums1

    def merge1(self, nums1, m, nums2, n):
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

    # nums1有足够空间容纳nums1和nums2
    a = [1, 2, 3, 4, 5, 0]
    m = 4
    b = [6, 7]
    n = 2
    s = Solution()
    print(s.merge(a, m, b, n))
