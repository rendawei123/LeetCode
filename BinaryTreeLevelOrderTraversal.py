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

