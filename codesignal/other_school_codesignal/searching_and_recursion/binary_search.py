"""
Given a sorted (in ascending order) integer array nums of n elements and a target value, write a function to search for target in nums. If target exists, then return its index, otherwise, return -1.

Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1

Note:

    All elements in nums are unique.
    The length of nums will be <= 100
    The value of each element in nums will be in the range [1, 10000]

    [execution time limit] 4 seconds (py3)

    [input] array.integer nums

    [input] integer target

    [output] integer
https://app.codesignal.com/solutions/rcErhXofxQXBwWSvZ?accessToken=riSN79DwWmRmwFk5H-Hu5f99RtDS89xqrHELWvwN4b

"""

def solution(nums, target):
    
    start = 0
    end = len(nums) - 1
    
    while start <= end:
        mid = (start + end) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return -1