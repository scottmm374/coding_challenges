"""
Note: Your solution should have O(l1.length + l2.length) time complexity, since this is what you will be asked to accomplish in an interview.

Given two singly linked lists sorted in non-decreasing order, your task is to merge them. In other words, return a singly linked list, also sorted in non-decreasing order, that contains the elements from both original lists.

Example

    For l1 = [1, 2, 3] and l2 = [4, 5, 6], the output should be
    solution(l1, l2) = [1, 2, 3, 4, 5, 6];
    For l1 = [1, 1, 2, 4] and l2 = [0, 3, 5], the output should be
    solution(l1, l2) = [0, 1, 1, 2, 3, 4, 5].

Input/Output

    [execution time limit] 4 seconds (py3)

    [input] linkedlist.integer l1

    A singly linked list of integers.

    Guaranteed constraints:
    0 ≤ list size ≤ 104,
    -109 ≤ element value ≤ 109.

    [input] linkedlist.integer l2

    A singly linked list of integers.

    Guaranteed constraints:
    0 ≤ list size ≤ 104,
    -109 ≤ element value ≤ 109.

    [output] linkedlist.integer

    A list that contains elements from both l1 and l2, sorted in non-decreasing order.

https://app.codesignal.com/solutions/BH3TdnWubvAHZZhto?accessToken=riSN79DwWmRmwFk5H-n5Xj2BATkbw3gxGtBjWTMvA3
"""

# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def solution(l1, l2):
    
    new_list = []
    curr = l1
    curr2 = l2
    
    while curr is not None:
        new_list.append(curr.value)
        curr = curr.next
        
    while curr2 is not None:
        new_list.append(curr2.value)
        curr2 = curr2.next
        
    sorted_list = sorted(new_list)    
    
    return sorted_list  
   
        
        
        
        
        
    
        
    
    
    