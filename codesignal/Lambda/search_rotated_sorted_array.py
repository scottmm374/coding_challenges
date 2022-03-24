"""
Given an integer array nums sorted in ascending order, and an integer target.

Suppose that nums is rotated at some pivot unknown to you beforehand (i.e., [1,2,3,4,5,6,7] might become [4,5,6,7,1,2,3]).

You should search for target in nums and if found return its index, otherwise return -1.

Example 1:
Input: nums = [6,7,1,2,3,4,5], target = 1
Output: 2

Example 2:
Input: nums = [6,7,1,2,3,4,5], target = 3
Output: 4

Example 3:
Input: nums = [1], target = 2
Output: -1

Your solution should have better than O(n) time complexity over the number of items in the list. There is an O(log n) solution. There is also an O(1) solution.

Note:

    1 <= nums.length < 100
    1 <= nums[i] <= 100
    All values of nums are unique.
    Numbers from 1 up to the length of the list will be contained in the list.

    [execution time limit] 4 seconds (py3)

    [input] array.integer nums

    [input] integer target

    [output] integer

https://app.codesignal.com/solutions/9gM6EKB65XWTabMwG?accessToken=riSN79DwWmRmwFk5H-Hu5f99RtDS89xqrHELWvwN4b
"""

def solution(nums, target):
    
    for x in range(len(nums)):
        if nums[x] == target:
            return x
            
    return -1
    
    # for x in range(len(nums)):
    #     if nums[x] - nums[x - 1] != 1:
    #         pivot = nums[x]    
    #         left = nums[x - 1]
    #         end = len(nums) - 1
    #         start = 0
            
    #         if target == pivot:
    #             return pivot
            
    #         if target < left and target > start:
    #             start = 0
    #             # print(nums[start], "start")
    #             end = x - 1
    #             # print(nums[end], "end")
                
    #             while start <= end:
    #                 mid = (end + start) // 2
                    
                    
    #                 if nums[mid] == target:
    #                     # print(mid)
    #                     return mid
            
    #                 if nums[mid] < target:
    #                     start = mid + 1
    #                 else:
    #                     end = mid - 1
                        
    #             return -1
                
                
    #         else:
                
    #             start = pivot
    #             end = len(nums) - 1
                
    #             while start <= end:
    #                 mid = (end + start) // 2
                    
    #                 if nums[mid] == target:
    #                     return mid
            
    #                 if nums[mid] < target:
    #                     start = mid + 1
    #                 else:
    #                     end = mid -1
                        
    #             return -1
                    
    # return -1      
           
        
    # print(nums[first_start], nums[first_end], nums[second_start], nums[second_end])
    
    
    # while  first_start <= first_end:
    #     mid = (first_end - first_start) // 2
        
    #     print(nums[mid], "mid")
    #     print(nums[first_start], "start")
    #     print(nums[first_end], "end")
    #     print("<--------------------------_>")
        
    #     if nums[mid] == target:
    #         return mid
            
    #     if nums[mid] < target:
    #         first_start = mid + 1
            
    #     else:
    #         first_end = mid -1
            
       
    # while second_start <= first_end:
    #     mid = (second_end - second_start) // 2
    #     if nums[mid] == target:
    #         return mid
            
    #     if nums[mid] < target:
    #         second_start = mid + 1
    #     else:
    #         second_end = mid -1
            
    # return -1
                