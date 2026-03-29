# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return 

        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        curr = slow.next
        slow.next = None
        prev = None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        first = head
        sec = prev

        while sec:
            tmp1 = first.next
            tmp2 = sec.next

            first.next = sec
            sec.next = tmp1

            first = tmp1
            sec = tmp2


            