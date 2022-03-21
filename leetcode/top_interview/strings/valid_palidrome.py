
def isPalindrome(self, s: str) -> bool:
        
        only_chars = "".join(x for x in s if x.isalnum()).lower()
        reverse_str = only_chars[::-1]
        
        if only_chars == reverse_str:
            return True
        return False

        
# Runtime: 55 ms 73.22%
# Memory Usage: 14.8 MB  40.76%


        