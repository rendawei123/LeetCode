"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.


判断是否是平衡二叉树

给定一个二叉树，判断它是否是高度平衡

高度平衡二叉树的定义：
二叉树的每个结点的两个子树的深度相差不大于一


解法：
采用递归算法

分别判断跟结点的两个子结点的结点深度是否相差大于一，
终结条件，如果没有子结点，返回0
"""




# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.check(root) != -1

    def check(self, root):

        if root is None:
            return 0

        left = self.check(root.left)
        right = self.check(root.right)

        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1

        return 1 + max(left, right)
