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

if __name__ == '__main__':

    # nums1有足够空间容纳nums1和nums2
    a = [1, 2, 3, 4, 5, 0]
    m = 4
    b = [6, 7]
    n = 2
    s = Solution()
    print(s.merge(a, m, b, n))