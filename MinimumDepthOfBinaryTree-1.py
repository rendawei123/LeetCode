"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path
from the root node down to the nearest leaf node.

Example
Given a binary tree as follow:

        1

     /     \

   2       3

          /    \

        4      5
The minimum depth is 2

题意：
求二叉树的最小深度

题解
注意审题，题中的最小深度指的是从根节点到最近的叶子节点（因为题中的最小深度是the number of nodes，故该叶子节点不能是空节点），所以需要单独处理叶子节点为空的情况。此题使用 DFS 递归实现比较简单。
"""

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if not root:
            return 0

        l_depth, r_depth = map(self.minDepth, (root.left, root.right))

        return (l_depth or r_depth) + 1

    def minDepth_1(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if root is None:
            return 0

        if root.left is None and root.right is None:
            return 1

        if root.left is None:
            return 1 + self.minDepth(root.right)

        if root.right is None:
            return 1 + self.minDepth(root.left)

        return min(1 + self.minDepth(root.left), 1 + self.minDepth(root.right))


class BinaryTreeNode:
    def __init__(self, data, left=None, right=None):
        self.value = data
        self.left = left
        self.right = right

if __name__ == '__main__':
    t = None
    t1 = BinaryTreeNode(1, BinaryTreeNode(2, BinaryTreeNode(2)), BinaryTreeNode(3))
    t2 = BinaryTreeNode(1, BinaryTreeNode(2))
    s = Solution()
    print(s.minDepth(t2))
