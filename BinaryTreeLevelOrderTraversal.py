"""
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]

题意：
遍历二叉树

解法：
使用回溯法遍历，
使用栈来作为缓存机构
采用深度优先法
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        stack = [(root, 0)]
        result = []
        while stack:
            node, level = stack.pop()

            if node:
                if len(result) < level+1:
                    result.insert(0, [])

                result[-(level+1)].append(node.val)
                stack.append((node.right, level+1))
                stack.append((node.left, level+1))

        return result
