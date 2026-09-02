# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        x = head
        xx = head

        while xx and xx.next:
            x = x.next
            xx = xx.next.next
            if x == xx:
                return True    

        return False