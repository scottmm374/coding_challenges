def firstUniqChar(s):
        
        char_dict = {}
        
        for x in range(len(s)):
            
            if s[x] not in char_dict:
                char_dict[s[x]] = 1
                
            else:
                char_dict[s[x]] +=1
   
        for x, y in char_dict.items():
            if y == 1:
                print(x)
                return s.index(x)
            
        return -1


# Runtime: 178 ms  Beats 41.40%
# Memory Usage: 14.2 MB beats 67.99%