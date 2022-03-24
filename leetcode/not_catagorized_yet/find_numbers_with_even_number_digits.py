def findNumbers(nums):
        count = 0
        for number in nums:
            
            length = len(str(number))
            
            if length % 2 == 0:
                count +=1
                
        return count


# Runtime: 77 ms beats 49.74%
# Memory Usage: 14.1 MB beats 24.26%

# 1295