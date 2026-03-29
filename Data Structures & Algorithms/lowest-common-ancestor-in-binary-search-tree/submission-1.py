# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Binary Search Tree property:
        ## For any node: left subtree values < node value
        ###             right subtree values > node value

        # For two nodes if both smaller than current node, go left
        #               if both larger than current node, go right
        # else the current node is the LCA

        while root:
            if p.val < root.val and q.val < root.val:
                root = root.left
            elif p.val >root.val and q.val > root.val:
                root = root.right

            else:
                return root