"""
Given a sorted array (in ascending order) of integers and a target, write a function that finds the two integers that add up to the target.

Examples:

    undefined([3,8,12,16], 11) -> [0,1]
    undefined([3,4,5], 8) -> [0,2]
    undefined([0,1], 1) -> [0,1]

Notes:

    Each input will have exactly one solution.
    You may not use the same element twice.

    [execution time limit] 4 seconds (py3)

    [input] array.integer numbers

    [input] integer target

    [output] array.integer
https://app.codesignal.com/solutions/Xocgjt45p4MKTHHHZ?accessToken=riSN79DwWmRmwFk5H-ekfqqLEKxN43Gdn94jai6Ksf
"""

def solution(numbers, target):
    
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if numbers[i] + numbers[j] == target:
                return (i, j)