import math

def sortedSquares(nums):
        
        for num in range(len(nums)):
            nums[num] = math.trunc(math.pow(nums[num], 2))
          
        new_arr = sorted(nums)
        return new_arr

# Runtime: 413 ms  beats 20.95%
# Memory Usage: 15.7 MB beats 93.87%