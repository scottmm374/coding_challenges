"""
Given a string, your task is to replace each of its characters by the next one in the English alphabet; i.e. replace a with b, replace b with c, etc (z would be replaced by a).

Example

For inputString = "crazy", the output should be solution(inputString) = "dsbaz".

Input/Output

    [execution time limit] 4 seconds (py3)

    [input] string inputString

    A non-empty string consisting of lowercase English characters.

    Guaranteed constraints:
    1 ≤ inputString.length ≤ 1000.

    [output] string

    The resulting string after replacing each of its characters.

https://app.codesignal.com/solutions/GNaZHPtWCXuxMYYea?accessToken=riSN79DwWmRmwFk5H-x9uofk9gddShdiTGvQwqt9ss
"""


def solution(inputString):
    new_str = ''
    
    for char in inputString:
        if char == 'z':
            new_char = 97
            new_str += chr(new_char)
        else:   
            new_char = ord(char) + 1
            new_str += chr(new_char)
    return new_str