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

        if not root:
            return []

        res = []
        q = deque([root])
        
        while q:
            level = []
            size = len(q)

            for _ in range(size):
                node = q.popleft()
                level.append(node.val)

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            res.append(level)

        return res







