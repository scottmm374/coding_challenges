"""
For a given positive integer n determine if it can be represented as a sum of two Fibonacci numbers (possibly equal).

Example

    For n = 1, the output should be
    solution(n) = true.

    Explanation: 1 = 0 + 1 = F0 + F1.

    For n = 11, the output should be
    solution(n) = true.

    Explanation: 11 = 3 + 8 = F4 + F6.

    For n = 60, the output should be
    solution(n) = true.

    Explanation: 60 = 5 + 55 = F5 + F10.

    For n = 66, the output should be
    solution(n) = false.

Input/Output

    [execution time limit] 4 seconds (py3)

    [input] integer n

    Guaranteed constraints:
    1 ≤ n ≤ 2 · 109.

    [output] boolean

    true if n can be represented as Fi + Fj, false otherwise.

https://app.codesignal.com/solutions/ZXEubpxkugE7eLm7t?accessToken=riSN79DwWmRmwFk5H-Hu5f99RtDS89xqrHELWvwN4b

"""

def solution(n):
    
    x = 50
 
    fibs = [0 for _ in range(0, x + 1)]
    fibs[0] = 0
    fibs[1] = 1

    for i in range(2, x + 1):
            fibs[i] = fibs[i - 1] + fibs[i - 2]
            
    print(fibs)     
    for x in fibs:
       
        if n - x in fibs:
            return True
            
    return False