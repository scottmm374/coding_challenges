"""
Given a number, write a function that converts that number into a string that contains "raindrop sounds" corresponding to certain potential factors. A factor is a number that evenly divides into another number, leaving no remainder. The simplest way to test if one number is a factor of another is to use the modulo operator.

Here are the rules for csRaindrop. If the input number:

    has 3 as a factor, add "Pling" to the result.
    has 5 as a factor, add "Plang" to the result.
    has 7 as a factor, add "Plong" to the result.
    does not have any of 3, 5, or 7 as a factor, the result should be the digits of the input number.

Examples:

    solution(28) -> "Plong"
        28 has 7 as a factor, but not 3 or 5.
    solution(30) -> "PlingPlang"
        30 has both 3 and 5 as factors, but not 7.
    solution(34) -> "34"
        34 is not factored by 3, 5, or 7.

    [execution time limit] 4 seconds (py3)

    [input] integer number

    [output] string

https://app.codesignal.com/solutions/u7Z92GvFGgTFzYDTk?accessToken=riSN79DwWmRmwFk5H-Ccq5NvLAYFThsZ978JYHxYTF
"""

def solution(number):
    print(number)
    sound = ""
    
    if number % 3 != 0 and number % 5 != 0 and number % 7 != 0:
        return str(number)
    if number % 3 == 0:
        sound += "Pling"
    if number % 5 == 0:
        sound += "Plang"
    if number % 7 == 0:
        sound += "Plong"
    return sound   