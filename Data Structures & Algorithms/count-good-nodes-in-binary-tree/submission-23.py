# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        max_so_far = float('-inf')

        def dfs(node, max_so_far):
            count = 0

            if not node:
                return count

            if node.val >= max_so_far:
                count += 1
                max_so_far = node.val

            count += dfs(node.left, max_so_far)
            count += dfs(node.right, max_so_far)
            return count

        
        return dfs(root, root.val)