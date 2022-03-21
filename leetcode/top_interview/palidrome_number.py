def isPalindrome(x):
        
        string = str(x)
        reversed = string[::-1]
        
        if string == reversed:
            return True
        
        return False

# Runtime: 84 ms  59.66%
# Memory Usage: 13.8 MB  97.47%


