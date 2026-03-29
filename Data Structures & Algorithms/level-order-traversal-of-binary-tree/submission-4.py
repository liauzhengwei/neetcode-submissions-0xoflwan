# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Visit nodes level by level, use Queue - BFS
        # 1. Put root node in a queue
        # 2. While queue not empty, get number of nodes in the current level
        ## process the nodes and add their children to the queue

        # Check if root exists
        if not root:
            return []

        res = []
        # Create the queue with 'root' initially
        q = deque([root])
        
        while q:
            level = []
            # Get the number of nodes in the current level
            size = len(q)

            for _ in range(size):
                node = q.popleft()
                # Add value to level
                level.append(node.val)

                # Add nodes if .left or .right exists
                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            # Add the 'level' array to the results array
            res.append(level)

        return res







