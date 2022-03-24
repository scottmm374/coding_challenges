"""
Given an integer, write a function that reverses the bits (in binary) and returns the integer result.

Examples:

    solution(417) -> 267
        417 in binary is 110100001. Reversing the binary is 100001011, which is 267 in decimal.
    solution(267) -> 417
    solution(0) -> 0

Notes:

    The input integer will not be negative.

    [execution time limit] 4 seconds (py3)

    [input] integer n

    [output] integer


https://app.codesignal.com/solutions/ggNBKsdZe592vbaKx?accessToken=riSN79DwWmRmwFk5H-Ccq5NvLAYFThsZ978JYHxYTF

"""

def solution(n):
    binary_num = str(bin(n)[2:])
    return int(binary_num[::-1], 2)