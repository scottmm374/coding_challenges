"""
Create a function that returns True if the given string has any of the following:

    Only letters and no numbers.
    Only numbers and no letters.

If a string has both numbers and letters or contains characters that don't fit into any category, return False.

Examples:

    solution("Bold") ➞ True
    solution("123454321") ➞ True
    solution("H3LL0") ➞ False

Notes:

    Any string that contains spaces or is empty should return False.

    [execution time limit] 4 seconds (py3)

    [input] string input_str

    [output] boolean
https://app.codesignal.com/solutions/xfF7odxhdtxtvkZHN?accessToken=riSN79DwWmRmwFk5H-oSMFqzhcyL2ZqgZPNFLE9xwZ

"""

def solution(input_str):
    if input_str.isalpha(): 
        return True
    elif input_str.isnumeric():
        print(input_str)
        return True
    else:
        return False