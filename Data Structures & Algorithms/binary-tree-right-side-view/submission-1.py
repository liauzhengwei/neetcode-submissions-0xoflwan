# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue = deque([root])
        rightList = []

        while queue:
            level_size = len(queue)
            for i in range(level_size):
                current = queue.popleft()

                if i == level_size - 1:
                    rightList.append(current.val)

                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)

        return rightList