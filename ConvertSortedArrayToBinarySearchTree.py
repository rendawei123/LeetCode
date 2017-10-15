"""
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

二叉查找树：
左子树的值小于根节点的值，根节点的值小于右子树的值

解法：
采用递归解法，从中间取值，由于本来就是按照顺序排列，左边自然就是左子树，右边是右子树
"""




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
