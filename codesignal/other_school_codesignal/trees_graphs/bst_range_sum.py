"""
You are given the root node of a binary search tree (BST).

You need to write a function that returns the sum of values of all the nodes with a value between lower and upper (inclusive).

The BST is guaranteed to have unique values.

Example 1:

Input:
root = [10, 5, 15, 3, 7, null, 18]
lower = 7
upper = 15

         10
         / \
        5  15
       / \    \
      3   7    18

Output:
32

Example 2:

Input:
root = [10,5,15,3,7,13,18,1,null,6]
lower = 6
upper = 10

           10
          /  \
       5       15
     / \     /   \ 
    3   7  13   18
   /   /
  1   6

Output:
23

    [execution time limit] 4 seconds (py3)

    [input] tree.integer root

    [input] integer lower

    [input] integer upper

    [output] integer


"""

# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def solution(root, lower, upper):
    sums = []
    if root.value >= lower and root.value <= upper:
            sums.append(root.value)
            
    def dft_tree(root):
        curr_node = root
        
        if curr_node.left:
            if curr_node.left.value >= lower and curr_node.left.value <= upper:
                sums.append(curr_node.left.value)
           
            dft_tree(curr_node.left)
                
        if curr_node.right:
            if curr_node.right.value >= lower and curr_node.right.value <= upper:
                sums.append(curr_node.right.value)
            dft_tree(curr_node.right)
            
             
    dft_tree(root)
    return sum(sums)