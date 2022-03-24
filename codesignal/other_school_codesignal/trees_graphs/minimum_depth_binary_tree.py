"""
You are given a binary tree and you are asked to write a function that finds its minimum depth. The minimum depth can be defined as the number of nodes along the shortest path from the root down to the nearest leaf node. As a reminder, a leaf node is a node with no children.

Example:
Given the binary tree [5,7,22,None,None,17,9],

    5
   / \
  7  22
    /  \
   17   9

your function should return its minimum depth = 2.

    [execution time limit] 4 seconds (py3)

    [input] tree.integer root

    [output] integer


"""

# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def solution(root):
        
    left_height = 0
    right_height = 0
    
    if root is None:
        return 0
        
    if root.right == None and root.left == None:
        return 1
        
    elif root.left:
        left_height = solution(root.left) + 1
        
    if root.right:
        right_height = solution(root.right) + 1
        
    if right_height == 0:
        return left_height
        
    elif left_height == 0:
        return right_height
        
    else:
        minimum_height = min(right_height, left_height)
        return minimum_height 
    