# Definition for a binary tree node.
class BinaryTreeNode:
    def __init__(self, data, left=None, right=None):
        self.value = data
        self.left = left
        self.right = right


class Solution(object):
    def hasPathSum(self, root, x):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False

        elif root.left is None and root.right is None:
            return x == root.value

        else:
            x -= root.value
            return self.hasPathSum(root.left, x) or self.hasPathSum(root.right, x)

if __name__ == '__main__':
    a = BinaryTreeNode(2, BinaryTreeNode(1, BinaryTreeNode(1)))
    s = Solution()
    print(s.hasPathSum(a, 4))