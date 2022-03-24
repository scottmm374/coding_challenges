"""
Note: Your solution should have O(n) time complexity, where n is the number of elements in l, and O(1) additional space complexity, since this is what you would be asked to accomplish in an interview.

Given a linked list l, reverse its nodes k at a time and return the modified list. k is a positive integer that is less than or equal to the length of l. If the number of nodes in the linked list is not a multiple of k, then the nodes that are left out at the end should remain as-is.

You may not alter the values in the nodes - only the nodes themselves can be changed.

Example

    For l = [1, 2, 3, 4, 5] and k = 2, the output should be
    solution(l, k) = [2, 1, 4, 3, 5];
    For l = [1, 2, 3, 4, 5] and k = 1, the output should be
    solution(l, k) = [1, 2, 3, 4, 5];
    For l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] and k = 3, the output should be
    solution(l, k) = [3, 2, 1, 6, 5, 4, 9, 8, 7, 10, 11].

Input/Output

    [execution time limit] 4 seconds (py3)

    [input] linkedlist.integer l

    A singly linked list of integers.

    Guaranteed constraints:
    1 ≤ list size ≤ 104,
    -109 ≤ element value ≤ 109.

    [input] integer k

    The size of the groups of nodes that need to be reversed.

    Guaranteed constraints:
    1 ≤ k ≤ l size.

    [output] linkedlist.integer

    The initial list, with reversed groups of k elements.

https://app.codesignal.com/solutions/E6KbuC5K9cQ6ovpLw?accessToken=riSN79DwWmRmwFk5H-n5Xj2BATkbw3gxGtBjWTMvA3
"""

# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def solution(l, k):
    
    i = 0
    counter = 0
    k_pos = 0
    final_list = []
    curr_node = l
    count_node = l


    while count_node is not None:
        count_node = count_node.next
        counter +=1
        
    remainder = counter % k
    new_list = []


    while i < counter - remainder:
        if k_pos <=k:
            new_list.append(curr_node.value)
            curr_node = curr_node.next
            k_pos +=1
        
        if k_pos == k:
            final_list.extend(new_list[::-1])
            new_list = []
            k_pos = 0
        i +=1
    i = 0
        
        
    curr_node = l
    
    
    while i <= len(final_list )-1:
        curr_node.value = final_list[i]
        curr_node = curr_node.next
        i += 1
    
    return l