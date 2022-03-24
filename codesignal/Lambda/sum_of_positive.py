"""
Given an array of integers, return the sum of all the positive integers in the array.

Examples:

    solution([1, 2, 3, -4, 5]) -> 1 + 2 + 3 + 5 = 11
    solution([-3, -2, -1, 0, 1]) -> 1
    solution([-3, -2]) -> 0

Notes:

    If the input_arr does not contain any positive integers, the default sum should be 0.

    [execution time limit] 4 seconds (py3)

    [input] array.integer input_arr

    [output] integer
https://app.codesignal.com/solutions/hQvsHiAbGKCT47Res?accessToken=riSN79DwWmRmwFk5H-nWRHYtQ7HAjAYAdsi2Zm9FMz

"""


def solution(input_arr):
    
    new_sum = 0
    for i in input_arr:
        print(i)
        if i > 0:
            new_sum += i
    return new_sum