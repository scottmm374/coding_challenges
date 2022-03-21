def longestCommonPrefix(strs):
        
        if len(strs) == 0:
            return " "
        
        ascend_list = sorted(strs, key=len)
        shortest = ascend_list[0]
        
        max_len = len(shortest)
       
        
        for string in ascend_list:
            index = 0
            while (index < max_len):
                if string[index] == shortest[index]:
                    index += 1
                else:
                    max_len = max_len -1
        prefix = shortest[0:max_len]
        
        if (len(prefix) == 0):
            return ""
        return prefix

# Runtime: 53 ms  beats 43.63%
# Memory Usage: 13.9 MB beats 92.06%