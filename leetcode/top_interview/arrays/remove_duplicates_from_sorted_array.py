def removeDuplicates(nums):
        

        count_unique = 1
        unique = 0
        current = 1
        
        if len(nums) == 1:
            return 1
        
        while (current < len(nums)):
            
            if nums[current] == nums[unique]:
                nums.pop(current) 
                
            else:
                unique = current
                count_unique += 1
                current = current + 1
                
                
        return count_unique


# Runtime: 148 ms  Beats 40.38 %
# Memory Usage: 15.5 MB  beats 69.85 %   then 24.63%?