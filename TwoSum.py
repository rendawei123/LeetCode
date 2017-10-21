"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

题目要求：
给出一个整数数组nums，和一个数target,假设数组里面有且只有两个数的和为target，求这两个数在数组中的索引,要求不能重复使用一个元素
"""


class Solution(object):
    # lowB法，两重循环挨个判断，效率很低
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

    # 由于只有唯一解，可以考虑利用字典的特性，两边扫描求解，第一遍扫描数组，将
    # 所有的数存放于一个字典中，字典中的建为数组的元素，值为元素在数组中的索引
    # 第二遍扫描数组,看数组中的每个元素num[i]看target-num[i]是否在字典中,若在，输出结果
    def two_sum_2(self, nums, target):
        d = {}
        for i in range(len(nums)):
            if target-nums[i] in d:
                return [d[target-nums[i]], i]
            else:
                d[nums[i]] = i

    # 第三种解法


if __name__ == '__main__':
    nums = [3, 2, 3]
    target = 6
    a = Solution()
    print(a.twoSum(nums, target))
