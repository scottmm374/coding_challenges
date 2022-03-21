

import msilib


def moveZeroes( nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        tracker = len(nums)
        
        x = 0
        while (x < tracker):
            if nums[x] == 0:
                zero = nums.pop(x)
                nums.append(zero)
                
                tracker -= 1
                if x == 0:
                    continue
                else:
                    
                    x -= 1
                
            else:
                x += 1
        print(nums)



# Runtime: 193 ms  Beats 73.22% python submissions
# Space beats 95.83% at 15.4 MB
