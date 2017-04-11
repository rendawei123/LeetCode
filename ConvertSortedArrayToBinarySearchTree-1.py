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
        if not nums:
            return None

        mid = len(nums) // 2

        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[: mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])

        return root


def print_binary_tree(root):
    if root is None:
        print('^', end='')
        return
    print('(' + str(root.val), end='')
    print_binary_tree(root.left)
    print_binary_tree(root.right)
    print(')', end='')

if __name__ == '__main__':
    a = [1, 2, 3, 4, 5]
    s = Solution()
    r = s.sortedArrayToBST(a)
    print_binary_tree(r)
