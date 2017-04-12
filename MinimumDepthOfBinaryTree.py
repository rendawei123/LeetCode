
class Solution(object):
    def minDepth(self, root):
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
