# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = [(root, float('-inf'), float('inf'))]

        while stack:
            current, min_val, max_val = stack.pop()
            if not (min_val < current.val < max_val):
                return False

            # Left child: max bound becomes current node
            if current.left:
                stack.append((current.left, min_val, current.val))
            
            # Right child: min bound becomes current node
            if current.right:
                stack.append((current.right, current.val, max_val))


        return True