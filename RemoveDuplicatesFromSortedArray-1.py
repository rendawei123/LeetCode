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

if __name__ == '__main__':
    nums = [1, 1, 2, 2, 3]
    a = Solution()
    print(a.removeDuplicates(nums))