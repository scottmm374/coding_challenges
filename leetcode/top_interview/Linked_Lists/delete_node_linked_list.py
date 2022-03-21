# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None



class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # copy the value of the node that is the next node we are given.
        node.val = node.next.val
        # then assign its next pointer to the node after the one being deleted
        node.next = node.next.next

        # This basically copies the next node value and pointer to the Node we are given, which overwrites its values, and in essence for this application "deletes" it. 


# Runtime: 56 ms, faster than 50.41% of Python3 online submissions for Delete Node in a Linked List.
# Memory Usage: 14.3 MB, less than 62.81% of Python3 online submissions for Delete Node in a Linked List.