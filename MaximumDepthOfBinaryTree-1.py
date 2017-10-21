"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the rootnode down to the farthest leaf node.

Example
Given a binary tree as follow:

  1
 / \
2   3
   / \
  4   5
The maximum depth is 3.

题意：
给一个二叉树：找到它的最大深度

解法：
使用递归进行深度优先遍历的牛逼解法
"""



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return 1 + max(map(self.maxDepth, (root.left, root.right))) if root else 0

    def maxDepth1(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root:
            return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
        else:
            return 0
