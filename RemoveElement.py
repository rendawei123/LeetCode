class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return 0

        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.remove(nums[i])
            else:
                i += 1

        return len(nums)

if __name__ == '__main__':
    num = [3, 2, 2, 3]
    val = 3
    a = Solution()
    print(a.removeElement(num, val))
