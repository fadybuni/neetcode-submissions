# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        ans = ListNode()
        res = ans
        
        while l1 or l2 or carry:
            if l1:
                a = l1.val
                l1 = l1.next
            else:
                a = 0
            if l2:
                b = l2.val
                l2 = l2.next
            else:
                b = 0

            curr = a + b + carry
            carry = 0
            if curr > 9:
                curr -= 10
                carry = 1
            res.next = ListNode(curr)
            res = res.next 
        return ans.next
