# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        curr1 = head

        while curr1 and curr1.next:
            curr = curr.next
            curr1 = curr1.next.next

            if curr == curr1:
                return True

        return False