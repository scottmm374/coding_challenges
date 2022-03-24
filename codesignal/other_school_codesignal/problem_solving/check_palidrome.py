"""
A palindrome is a word, phrase, number, or another sequence of characters that reads the same backward or forward. This includes capital letters, punctuation, and other special characters.

Given a string, write a function that checks if the input is a valid palindrome.

Examples:

    solution("racecar") -> true
    solution("anna") -> true
    solution("12345") -> false
    solution("12321") -> true

Notes:

    Try to solve this challenge without using the reverse of the input string; use a for loop to iterate through the string and make the necessary comparisons.
    Something like the code below might be your first intuition, but can you figure out a way to use a for loop instead?

def solution(input_str):
    return input_str == "".join(reversed(input_str))

    [execution time limit] 4 seconds (py3)

    [input] string input_str

    [output] boolean

https://app.codesignal.com/solutions/FHSzgSNnrxu9SscWm?accessToken=riSN79DwWmRmwFk5H-7ZXpBLY2EL72pqrMJRA6Y2R3
"""


def solution(input_str):
    new_str = input_str[::-1]
    
    if new_str == input_str:
        return True
    return False