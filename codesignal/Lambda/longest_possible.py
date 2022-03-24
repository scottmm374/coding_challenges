"""
Given two strings that include only lowercase alpha characters, str_1 and str_2, write a function that returns a new sorted string that contains any character (only once) that appeared in str_1 or str_2.

Examples:

    solution("aabbbcccdef", "xxyyzzz") -> "abcdefxyz"
    solution("abc", "abc") -> "abc"

    [execution time limit] 4 seconds (py3)

    [input] string str_1

    [input] string str_2

    [output] string

https://app.codesignal.com/solutions/faBvAiFJthPTg8zX2?accessToken=riSN79DwWmRmwFk5H-nWRHYtQ7HAjAYAdsi2Zm9FMz

"""


def solution(str_1, str_2):
    combine_str = (str_1 + str_2)
    new_set = set(combine_str)
    sorted_set = sorted(new_set)
    longest = ''.join(sorted_set)
    return longest