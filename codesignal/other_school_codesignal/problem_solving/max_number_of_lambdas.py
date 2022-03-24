"""
Given a string text, you need to use the characters of text to form as many instances of the word "lambda" as possible.

You can use each character in text at most once.

Write a function that returns the maximum number of instances of "lambda" that can be formed.

Example 1:

Input: text = "mbxcdatlas"
Output: 1

Example 2:

Input: text = "lalaaxcmbdtsumbdav"
Output: 2

Example 3:

Input: text = "sctlamb"
Output: 0

Notes:

    text consists of lowercase English characters only

    [execution time limit] 4 seconds (py3)

    [input] string text

    [output] integer


"""


def solution(text):
    
    x = "lambda"
    
    # creating a dictionary with char of Lambda as keys, No need to worry about other characters. 
    lambda_dict = dict.fromkeys(x, 0)
    
    # Then just checking and adding how many times each character of Lambda shows up.
    for i in text:
        if i in lambda_dict:
            lambda_dict[i] += 1
            
    # returning min value, since thats how many times a complete Lambda can be created. 
    num_of_lambdas = min(lambda_dict.values())

    return num_of_lambdas