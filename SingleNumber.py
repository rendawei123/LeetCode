class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in nums:
            if nums.count(i) < 2:
                return i

if __name__ == '__main__':
    l = [1,1,2,2,3,3,4]
    a = Solution()
    print(a.singleNumber(l))
