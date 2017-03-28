class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        max_sum = cur_sum = nums[0]

        for each in nums[1:]:
            cur_sum = max(each, cur_sum + each)
            max_sum = max(max_sum, cur_sum)

        return max_sum

if __name__ == '__main__':
    l1 = [-9, 1, 5, -2, 7]
    a = Solution()
    print(a.maxSubArray(l1))