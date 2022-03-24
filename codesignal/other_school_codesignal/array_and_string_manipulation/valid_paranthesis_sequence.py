"""
You are given a parentheses sequence, check if it's regular.

Example

    For s = "()()(())", the output should be
    solution(s) = true;
    For s = "()()())", the output should be
    solution(s) = false.

Input/Output

    [execution time limit] 4 seconds (py3)

    [input] string s

    A string, consisting only of '(' and ')'.

    Guaranteed constraints:
    0 ≤ s.length ≤ 105.

    [output] boolean

    true is the sequence is regular and false otherwise.

https://app.codesignal.com/solutions/Wh8ENyrLvtutgrFTt?accessToken=riSN79DwWmRmwFk5H-x9uofk9gddShdiTGvQwqt9ss

"""

def solution(s):
    if len(s) % 2 != 0:
        return False
       
    right_count = 0
    left_count = 0 
    for x, y in enumerate(s):
        if s[0] == ')' or s[-1] == '(':
            return False
        if y == '(':
            left_count += 1
        if y == ')':
            right_count += 1
    if right_count == left_count:
        return True