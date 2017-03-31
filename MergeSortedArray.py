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