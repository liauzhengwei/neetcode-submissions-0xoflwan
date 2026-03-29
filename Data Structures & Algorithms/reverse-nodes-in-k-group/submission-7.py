# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = 0
        curr = head

        while curr:
            length += 1
            curr = curr.next

        dummy = ListNode(0)
        dummy.next = head
        prev_group = dummy

        while length >= k:
            group_start = prev_group.next
            group_end = group_start

            for _ in range(k - 1):
                group_end = group_end.next

            next_group = group_end.next

            prev = next_group
            curr = group_start

            while curr != next_group:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            prev_group.next = group_end
            prev_group = group_start

            length -= k

        return dummy.next    