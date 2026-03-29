# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
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

        fir = head
        sec = prev

        while sec:
            tmp1 = fir.next
            tmp2 = sec.next

            fir.next = sec
            sec.next = tmp1

            fir = tmp1
            sec = tmp2

        
    
