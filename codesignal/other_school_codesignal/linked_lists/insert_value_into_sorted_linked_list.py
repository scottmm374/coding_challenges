"""
Note: Your solution should have O(n) time complexity, where n is the number of elements in l, since this is what you will be asked to accomplish in an interview.

You have a singly linked list l, which is sorted in strictly increasing order, and an integer value. Add value to the list l, preserving its original sorting.

Note: in examples below and tests preview linked lists are presented as arrays just for simplicity of visualization: in real data you will be given a head node l of the linked list

Example

    For l = [1, 3, 4, 6] and value = 5, the output should be
    solution(l, value) = [1, 3, 4, 5, 6];
    For l = [1, 3, 4, 6] and value = 10, the output should be
    solution(l, value) = [1, 3, 4, 6, 10];
    For l = [1, 3, 4, 6] and value = 0, the output should be
    solution(l, value) = [0, 1, 3, 4, 6].

Input/Output

    [execution time limit] 4 seconds (py3)

    [input] linkedlist.integer l

    A singly linked list of integers sorted in strictly increasing order. Thus, all integers in the list are pairwise distinct.

    Guaranteed constraints:
    0 ≤ list size ≤ 104,
    -109 ≤ element value ≤ 109.

    [input] integer value

    A single integer value to be inserted into l. It is guaranteed that there is not an element equal to value in l before the insertion is performed.

    Guaranteed constraints:
    -109 ≤ value ≤ 109.

    [output] linkedlist.integer

    Return l after inserting value into it, with the original sorting preserved.

https://app.codesignal.com/solutions/G2chDD5sJeueDpj4R?accessToken=riSN79DwWmRmwFk5H-n5Xj2BATkbw3gxGtBjWTMvA3
"""

# Singly-linked lists are already defined with this interface:
class ListNode(object):
  def __init__(self, x):
    self.value = x
    self.next = None

def solution(l, value):
    curr_node = l
    new_node = ListNode(value)
    
    # if empty list
    if curr_node is None: 
        l = new_node
        return l
            
      
    while curr_node is not None:  
        if value < curr_node.value:
            new_node.next = curr_node
            l = new_node
            return l
            
        if curr_node.next is None:
            curr_node.next = new_node
            return l
        
        if value > curr_node.value and value < curr_node.next.value:
            new_node.next = curr_node.next
            curr_node.next = new_node
            return l
            

        curr_node = curr_node.next
    return l    