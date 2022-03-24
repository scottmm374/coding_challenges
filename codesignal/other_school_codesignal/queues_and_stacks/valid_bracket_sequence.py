"""
Given a string sequence consisting of the characters '(', ')', '[', ']', '{', and '}'. Your task is to determine whether or not the sequence is a valid bracket sequence.

The Valid bracket sequence is defined in the following way:

    An empty bracket sequence is a valid bracket sequence.
    If S is a valid bracket sequence then (S), [S] and {S} are also valid.
    If A and B are valid bracket sequences then AB is also valid.

Example

    For sequence = "()", the output should be solution(sequence) = true;
    For sequence = "()[]{}", the output should be solution(sequence) = true;
    For sequence = "(]", the output should be solution(sequence) = false;
    For sequence = "([)]", the output should be solution(sequence) = false;
    For sequence = "{[]}", the output should be solution(sequence) = true.

Input/Output

    [execution time limit] 4 seconds (py3)

    [input] string sequence

    A bracket sequence, consisting of the characters (, ), [, ], {, and }.

    Guaranteed constraints:
    0 ≤ sequence.length ≤ 106.

    [output] boolean

    true if sequence is a valid bracket sequence and false otherwise.


"""


def solution(sequence):
    
    my_dict = {'(': 0, ')': 0,'[': 0 , ']': 0 , '{': 0 , '}': 0 }
    count = 0

  
    if len(sequence) <= 0:
        return True
        
    if len(sequence) % 2 != 0:
        return False
        
    if sequence[0] == ')' or sequence[0] == ']' or sequence[0] == '}' or sequence[-1] == '(' or sequence[-1] == '[' or sequence[-1] == '{':
        return False
        
    x = 0  
    while x < len(sequence):
        
    
        if sequence[x] == "(" and sequence[x + 1] == "]" or  sequence[x] == "(" and sequence[x + 1] == "}":
            return False
        if sequence[x] == "[" and sequence[x + 1] == ")" or  sequence[x] == "[" and sequence[x + 1] == "}":
            return False
        if sequence[x] == "{" and sequence[x + 1] == "]" or  sequence[x] == "{" and sequence [x + 1]== ")":
            return False
        if sequence[x] in my_dict:
            my_dict[sequence[x]] +=1
        
        x += 1
        
    if my_dict['('] == my_dict[')'] and  my_dict['['] == my_dict[']'] and  my_dict['{'] == my_dict['}']:
        return True
    return False
        
    