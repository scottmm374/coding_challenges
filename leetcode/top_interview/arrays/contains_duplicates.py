def containsDuplicate( nums):
        
        remove_dups = set(nums)
        
        if len(nums) == len(remove_dups):
            return False
        
        return True


# Runtime: 515 ms  beats 69.30%
# Memory Usage: 25.9 MB beats 69.61%