# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1, p2 = list1, list2
        initial = None
        new = None
#initial
        while p1 or p2:
            if (p1.val if p1 else float('inf')) < (p2.val if p2 else float('inf')):
                if not new:
                    new = p1
                    initial = new
                else:
                    new.next = p1
                    new = new.next
                p1 = p1.next
            else:
                if not new:
                    new = p2
                    initial = new
                else:
                    new.next = p2
                    new = new.next
                p2 = p2.next
        
        return initial
            



        
            