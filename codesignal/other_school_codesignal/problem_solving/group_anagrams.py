"""
Given an array of strings strs, write a function that can group the anagrams. The groups should be ordered such that the larger groups come first, with subsequent groups ordered in descending order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input:
strs = ["apt","pat","ear","tap","are","arm"]

Output:
[["apt","pat","tap"],["ear","are"],["arm"]]

Example 2:

Input:
strs = [""]

Output:
[[""]]

Example 3:

Input:
strs = ["a"]

Output:
[["a"]]

Notes:

    strs[i] consists of lower-case English letters.

    [execution time limit] 4 seconds (py3)

    [input] array.string strs

    [output] array.array.string


"""


def solution(strs):
    
    if len(strs) <= 1:
        return [strs]
        
    anogram_dict = {}
    
    for word in strs:
        uni = sum(ord(char) for char in word)
        if uni not in anogram_dict:
            anogram_dict[uni] = []
            
        anogram_dict[uni] +=[word]
        
    results = []   
    for key, value in anogram_dict.items():
        results.append(value)
        
   
    return results
        