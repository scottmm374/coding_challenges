def plusOne(digits):
        
        string = ""
        digit_list = []
        
        for x in digits:
            string += str(x)
            
        add_one = int(string) + 1
            
            
        for digit in str(add_one):
            digit_list.append(int(digit))
            
        return digit_list

# Runtime: 34 ms  beats 84.50%
# Memory Usage: 13.9 MB beats 25.60%