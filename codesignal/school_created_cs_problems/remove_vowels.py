"""
Given a string, return a new string with all the vowels removed.

Examples:

    undefined("Lambda School is awesome!") -> "Lmbd Schl s wsm!"

Notes:

    For this challenge, "y" is not considered a vowel.

    [execution time limit] 4 seconds (py3)

    [input] string input_str

    [output] string


https://app.codesignal.com/solutions/xkfxbRezLYoZwCeYK?accessToken=riSN79DwWmRmwFk5H-nWRHYtQ7HAjAYAdsi2Zm9FMz

"""


def solution(input_str):
    new_str = input_str
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    for char in new_str:
        if char.lower() in vowels or char in vowels:
            new_str = new_str.replace(char, '')
        
    return new_str