"""
Given two strings a and b, determine if they are isomorphic.

Two strings are isomorphic if the characters in a can be replaced to get b.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

Example 1:

Input: 
a = "odd"
b = "egg"

Output:
true

Example 2:

Input:
a = "foo"
b = "bar"

Output:
false

Example 3:

Input:
a = "abca"
b = "zbxz"

Output:
true

Example 4:

Input:
a = "abc"
b = ""

Output:
false

    [execution time limit] 4 seconds (py3)

    [input] string a

    [input] string b

    [output] boolean


"""


def solution(a, b):
    
    #  checking strings to see if they are equal, or empty. 
    if len(a) != len(b):
        return False
     
    # creating sets and comparing length, if one is larger then the other, then characters are not being repeated isomentrically    
    word = set(a)
    word2 = set(b)
    
    if len(word) != len(word2):
        return False
        
    return True
        
   