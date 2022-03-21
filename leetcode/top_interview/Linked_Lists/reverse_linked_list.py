# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev = None
        current = head
        temp = None
        
        while(current is not None):
#           stores node after current, so that we can point current node towards prev
            temp = current.next
#           change current pointer to prev node reversing pointer
            current.next = prev
#           move prev, one node to current, and current to temp node
            prev = current
            current = temp
        
        return prev


# Runtime: 81 ms beats 5.41% 
# Memory Usage: 15.4 MB beats 95.88%