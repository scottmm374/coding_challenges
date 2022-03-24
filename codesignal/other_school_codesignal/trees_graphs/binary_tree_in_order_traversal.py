"""
You are given a binary tree. Write a function that returns the binary tree's node values using an in-order traversal.

Example:
Input: [2,None,3,4]

   2
    \
     3
    /
   4

Output: [2,4,3]

    [execution time limit] 4 seconds (py3)

    [input] tree.integer root

    [output] array.integer


"""

# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def solution(root):
    
    stack = []
    curr_node = root
   
    def in_order(curr_node):
        if curr_node.left:
            in_order(curr_node.left)
            
        stack.append(curr_node.value)
        
        if curr_node.right:
            in_order(curr_node.right)
            
    in_order(root)
    return stack