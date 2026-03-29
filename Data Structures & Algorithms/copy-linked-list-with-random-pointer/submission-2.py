"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        
        # Add new nodes interleaved into the original list
        curr = head

        while curr is not None:
            new_node = Node(curr.val)
            new_node.next = curr.next
            curr.next = new_node
            curr = new_node.next

        # Set the random pointer for the two nodes
        new_head = head.next
        curr = head


        while curr is not None:
            if curr.random is not None:
                curr.next.random = curr.random.next
            curr = curr.next.next

        # Separate the two lists
        curr = head

        while curr is not None:
            curr1 = curr.next
            curr.next = curr1.next
            if curr1.next is not None:
                curr1.next = curr1.next.next
            curr = curr.next

        return new_head

