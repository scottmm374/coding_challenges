# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current = head
#       if only one node in linked list
        if current.next == None:
            current.value = None
            return
        
        
        current = head
        length = 1

#       get length of linked list
        while(current.next is not None):
            current = current.next
            length = length + 1
            
      # if the target is == to the head
        current = head
        if length == n:
            current.val = None
            head = current.next
            
            return head
            
#       stop at Node previous to target node 
        target_node_index = length - n
#       reset current back to head to find target node
        current = head
        count = 1
        while(count != target_node_index):
            count +=1
            current = current.next
        current.next.val = None
        current.next = current.next.next
        
        return head


# Runtime: 46 ms  beats 55.44%
# Memory Usage: 13.9 MB beats 78.18%