# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack1 = []
        stack2 = []

        curr1 = l1
        curr2 = l2

        while curr1: 
            stack1.append(curr1.val)
            curr1 = curr1.next  #123, actl 321

        while curr2:
            stack2.append(curr2.val)
            curr2 = curr2.next  #456, actl 654

        count = 0
        num1 = 0
        while stack1:
            currNum = stack1.pop(0)
            num1 = num1 + (10 ** count) * currNum
            count += 1

        count = 0
        num2 = 0
        while stack2:
            currNum = stack2.pop(0)
            num2 = num2 + (10 ** count) * currNum
            count += 1

        sumnum = num1 + num2

        if sumnum == 0:
            return ListNode(0)

        # turn the sumnum into a linked list
        dummy = ListNode(0)   # 579, actl 975
        curr = dummy
        while sumnum:
            remainder = sumnum % 10
            curr.next = ListNode(remainder)
            curr = curr.next
            sumnum = sumnum // 10

        return dummy.next

