def isAnagram(self, s: str, t: str) -> bool:
        
        freq_dict = {}
        
        if len(s) != len(t):
            return False
        
        for x in range(len(s)):
            if s[x] not in freq_dict:
                freq_dict[s[x]] = 1
            else:
                freq_dict[s[x]] += 1
                
        for j in range(len(t)):
            if t[j] in freq_dict:
                freq_dict[t[j]] -=1
          
    
        for key, val in freq_dict.items():
            if val != 0:
                return False
            
        return True

# Runtime: 100 ms  14.55%
# Memory Usage: 14.4 MB  71.18%