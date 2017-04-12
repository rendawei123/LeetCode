
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
