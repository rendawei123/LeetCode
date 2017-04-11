# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if nums == []:
            return None

        index = len(nums) // 2
        root_num = nums[index]
        left_nums = nums[: index]

        if index + 1 == len(nums):
            right_nums = []
        else:
            right_nums = nums[index+1:]

        root = TreeNode(root_num)
        root.left = self.sortedArrayToBST(left_nums)
        root.right = self.sortedArrayToBST(right_nums)

        return root

