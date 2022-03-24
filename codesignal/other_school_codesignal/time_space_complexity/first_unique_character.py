"""
Given a string, write a function that returns the index of the first unique (non-repeating) character. If there isn't a unique (non-repeating) character, return -1.

Examples:

    solution(input_str = "lambdaschool") -> 2
    solution(input_str = "ilovelambdaschool") -> 0
    solution(input_str = "vvv") -> -1

Notes:

    input_str will only contain lowercase alpha characters.

    [execution time limit] 4 seconds (py3)

    [input] string input_str

    [output] integer

https://app.codesignal.com/solutions/DsDtBT5wFWu865XiN?accessToken=riSN79DwWmRmwFk5H-ekfqqLEKxN43Gdn94jai6Ksf

"""

def solution(input_str):
    letters = {}
    
    if len(input_str) < 1:
        return -1
        
    for char in input_str:
        if char in letters:
            letters[char] +=1
        else:
            letters[char] = 1 

    for key, value in letters.items():
        if value == 1:
           return input_str.index(key)
           
    return -1