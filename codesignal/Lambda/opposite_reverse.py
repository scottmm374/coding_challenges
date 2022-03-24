"""
Write a function that takes a string as input and returns that string in reverse order, with the opposite casing for each character within the string.

Examples:

    solution("Hello World") ➞ "DLROw OLLEh"
    solution("ReVeRsE") ➞ "eSrEvEr"
    solution("Radar") ➞ "RADAr"

Notes:

    The input string will only contain alpha characters.

    [execution time limit] 4 seconds (py3)

    [input] string txt

    [output] string

https://app.codesignal.com/solutions/Y6uv5eBAsH57bvaiq?accessToken=riSN79DwWmRmwFk5H-oSMFqzhcyL2ZqgZPNFLE9xwZ
"""


def solution(txt):

    str = txt[::-1]
    return str.swapcase()