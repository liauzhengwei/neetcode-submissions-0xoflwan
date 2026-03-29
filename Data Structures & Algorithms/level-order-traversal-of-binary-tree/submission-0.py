# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        lvlordlist = []
        queue = deque([root]) # start with root node

        while queue:
            level_size = len(queue)
            level_nodes = []

            for _ in range(level_size):
                current = queue.popleft()
                level_nodes.append(current.val)

                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)

            lvlordlist.append(level_nodes)

        return lvlordlist