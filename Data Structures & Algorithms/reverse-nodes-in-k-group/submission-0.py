# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        grp_prev = dummy

        while True:
            kth = self.get_k_node(grp_prev,k)
            if not kth:
                break
            grp_next = kth.next

            # Reverse the ListNodes
            prev, curr = kth.next, grp_prev.next
            while curr != grp_next:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            # Update the pointers
            tmp = grp_prev.next # saves the old start aka end after reversal
            grp_prev.next = kth # link the end to the new start
            grp_prev = tmp  # keep the old start for next look

        return dummy.next

    def get_k_node(self, curr, k):
        while curr and k>0:
            k-=1
            curr = curr.next
        return curr