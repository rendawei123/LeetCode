# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# 题目要求：给出一个整数数组nums，和一个数target,假设数组里面有且只有两个数的和为target，求这两个数在数组中的索引,要求不能重复使用一个元素
# 这种做法是比较lowb的方法，让k等于列表末尾的一个数，用第一个数分别和后面所有
# 的数比较，看时候符合题意，然后用第二个数和后面所有的数比较，如果符合题意则输出序号
# 这种方法超出了时间，效率比较慢


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
