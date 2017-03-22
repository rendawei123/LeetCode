class Solution(object):
    def twoSum(self, nums, target):
        i = 0
        j = 1
        k = len(nums) - 1
        result = []
        while True:
            if nums[i] + nums[j] == target:
                result.append(i)
                result.append(j)
                break
            j += 1
            if j > k:
                i += 1
                j = i + 1
            if i == k:
                break
        if result:
            return result
        else:
            return None

if __name__ == '__main__':
    nums = [3, 2, 3]
    target = 6
    a = Solution()
    print(a.twoSum(nums, target))
