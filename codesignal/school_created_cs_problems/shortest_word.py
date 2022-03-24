"""
Given a string of words, return the length of the shortest word(s).

Notes:

    The input string will never be empty and you do not need to validate for different data types.

    [execution time limit] 4 seconds (py3)

    [input] string input_str

    [output] integer

https://app.codesignal.com/solutions/B3HiqtKqqgogh488t?accessToken=riSN79DwWmRmwFk5H-nWRHYtQ7HAjAYAdsi2Zm9FMz

"""

def solution(input_str):
    new_str = input_str.split()
    new_str.sort(key=len)
    return len(new_str[0])