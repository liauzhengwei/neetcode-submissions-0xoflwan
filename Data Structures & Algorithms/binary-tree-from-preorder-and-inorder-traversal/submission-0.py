# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder = root, left, right
        # inorder = left, root, right
        
        # Map value to index in inorder 
        inorder_index = {val:i for i, val in enumerate(inorder)}

        # Use an iterator for preorder
        preorder_index = 0

        def helper(left, right):
            nonlocal preorder_index # value comes from closest enclosing function scope
            # No elemets left to construct the tree
            if left > right:
                return None

            root_val = preorder[preorder_index]
            preorder_index += 1
            root = TreeNode(root_val)
                
            root.left = helper(left, inorder_index[root_val]-1)
            root.right = helper(inorder_index[root_val]+1, right)

            return root

        return helper(0, len(inorder)-1)