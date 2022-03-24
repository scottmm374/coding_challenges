"""
Given a binary string (ASCII encoded), write a function that returns the equivalent decoded text.

Every eight bits in the binary string represents one character on the ASCII table.

Examples:

    solution("011011000110000101101101011000100110010001100001") -> "lambda"
        01101100 -> 108 -> "l"
        01100001 -> 97 -> "a"
        01101101 -> 109 -> "m"
        01100010 -> 98 -> "b"
        01100100 -> 100 -> "d"
        01100001 -> 97 -> "a"
    solution("") -> ""

Notes:

    The input string will always be a valid binary string.
    Characters can be in the range from "00000000" to "11111111" (inclusive).
    In the case of an empty input string, your function should return an empty string.

    [execution time limit] 4 seconds (py3)

    [input] string binary

    [output] string

https://app.codesignal.com/solutions/6vkEw6LY3r8Mfc2fT?accessToken=riSN79DwWmRmwFk5H-Ccq5NvLAYFThsZ978JYHxYTF

"""

def solution(binary):
    letter_list = []
    i = 0
    count = 0
    new_str = ''
    
    while i < len(binary):
        count += 1
        new_str += binary[i]
        if count == 8:
            letter_list.append(chr(int(new_str, 2)))
            new_str = " "
            count = 0
            
        i +=1
    return "".join(letter_list)