class Solution(object):
    def removeDuplicates(self, nums):
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
    nums = [1, 1, 2]
    a = Solution()
    print(a.removeDuplicates(nums))