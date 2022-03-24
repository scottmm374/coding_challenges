"""
Given a start integer and an ending integer (both inclusive), write a function that returns the count (not the sum) of all integers in the range (except integers that contain the digit 5).

Examples:

    solution(1, 5) -> 1, 2, 3, 4, -> 4 (there are 4 integers in the range that do not contain the digit 5)
    solution(1, 9) -> 1, 2, 3, 4, 6, 7, 8, 9 -> 8
    solution(4, 17) -> 4,6,7,8,9,10,11,12,13,14,16,17 -> 12

Notes:

    The output can contain the digit 5.
    The start number will always be less than the end number (both numbers can also be negative).

    [execution time limit] 4 seconds (py3)

    [input] integer start

    [input] integer end

    [output] integer

https://app.codesignal.com/solutions/f3MCdFiXvCv97JHu4?accessToken=riSN79DwWmRmwFk5H-nWRHYtQ7HAjAYAdsi2Zm9FMz

"""


def solution(start, end):
    
    count = 0
    for i in range(start, end + 1):
        x = str(i)
        if '5' in x:
            continue
            
        else:
            count +=1
    return count