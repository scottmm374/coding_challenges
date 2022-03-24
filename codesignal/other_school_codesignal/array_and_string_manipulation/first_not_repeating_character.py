# Given a string s consisting of small English letters, find and return the first instance of a non-repeating character in it. If there is no such character, return '_'.

# Example

#     For s = "abacabad", the output should be
#     solution(s) = 'c'.

#     There are 2 non-repeating characters in the string: 'c' and 'd'. Return c since it appears in the string first.

#     For s = "abacabaabacaba", the output should be
#     solution(s) = '_'.

#     There are no characters in this string that do not repeat.

#     [execution time limit] 4 seconds (py3)

#     [input] string s

#     A string that contains only lowercase English letters.

#     [output] char

#     The first non-repeating character in s of '_' if there are no characters that do not repeat.
# https://app.codesignal.com/solutions/HTANMC8nhcgmXBXCy?accessToken=riSN79DwWmRmwFk5H-kbQAifKXJZ9PQobJAcHJMH5y

def solution(s):
    
    no_repeat_dict = {}
    if len(s) == 0:
        return '_'
    
    for char in s:
        if char in no_repeat_dict:
            no_repeat_dict[char] += 1
        else:
            no_repeat_dict[char] = 1
            
    for key, value in no_repeat_dict.items():
 
        if value != 1:
            continue
            
        if value == 1:
            return key
            
    return '_'

# <--------------------------------I Solved this one twice I guess, second solution below ---------------->

    # def solution(s):

    # count = {}
    
    # for char in s:
    #     if char in count:
    #         count[char] +=1
            
    #     else:
    #         count[char] = 1
            
            
    # for key, value in count.items():
    #     print(key, value)
        
    #     if value == 1:
    #         return key
              
    # return '_'