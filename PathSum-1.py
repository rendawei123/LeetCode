"""
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.


题意：
路径之和，给一个二叉树和一个总和，判断有一条从根结点到叶结点的路径的值的和为给定的总和

采用递归深度优先遍历法，然后进行判断，但是这种方法比较麻烦的一点就是，二叉树的每个分支都要求和进行判断，所以需要挨个求出每条路径的和，这个效率太低

我们可以反其道而行之，同样是递归，我们可以使用给定的数sum减去根结点，然后判断左右两个子树中是否有路径之和等于sum减去root，这样，大大减少来运算的复杂成都
"""



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
