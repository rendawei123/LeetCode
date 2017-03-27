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
        else:
            return 0

if __name__ == '__main__':
    nums = [1]
    target = 0
    a = Solution()
    print(a.searchInsert(nums, target))
