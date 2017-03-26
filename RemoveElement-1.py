class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        start, end = 0, len(nums)-1
        while start <= end:
            if nums[start] == val:
                nums[start], nums[end], end = nums[end], nums[start], end-1
            else:
                start += 1
        return start

if __name__ == '__main__':
    num = [3, 2, 2, 3]
    val = 3
    a = Solution()
    print(a.removeElement(num, val))
