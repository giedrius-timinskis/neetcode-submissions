# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        next = head
        prev = None

        while next:
            curr = next
            next = curr.next
            curr.next = prev
            prev = curr

        return prev
            
            
            
        