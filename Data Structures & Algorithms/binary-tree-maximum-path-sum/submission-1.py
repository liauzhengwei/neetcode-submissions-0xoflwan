# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Traverse the tree with DFS
        # At each node:
        ## recursively get the left and right gains
        ## update the global max
        ## return to parent

        self.max_sum = float('-inf')
        def dfs(node):
            if not node:
                return 0

            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)

            # Path passing through this node
            current_sum = node.val + left + right

            # Update global max
            self.max_sum = max(self.max_sum, current_sum)

            # Return max gain to parent
            return node.val + max(left, right)

        dfs(root)
        return self.max_sum