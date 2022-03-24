"""
You are given a two-digit integer n. Return the sum of its digits.

Example

For n = 29, the output should be
solution(n) = 11.

Input/Output

    [execution time limit] 4 seconds (py3)

    [input] integer n

    A positive two-digit integer.

    Guaranteed constraints:
    10 ≤ n ≤ 99.

    [output] integer

    The sum of the first and second digits of the input number.

[Python 3] Syntax Tips

https://app.codesignal.com/arcade/code-arcade/intro-gates/wAGdN6FMPkx7WBq66

"""


def solution(n):
    sum = 0
    for digit in str(n):   
      sum += int(digit)        
    return sum