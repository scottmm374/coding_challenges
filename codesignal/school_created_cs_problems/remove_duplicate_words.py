"""
Given a string, write a function that removes all duplicate words from the input. The string that you return should only contain the first occurrence of each word in the string.

Examples:

    `solution("alpha bravo bravo golf golf golf delta alpha bravo bravo golf golf golf delta") -> "alpha bravo golf delta"
    `solution("my dog is my dog is super smart") -> "my dog is super smart"

    [execution time limit] 4 seconds (py3)

    [input] string input_str

    [output] string

https://app.codesignal.com/solutions/ARcXZ8vAK2TetBrhF?accessToken=riSN79DwWmRmwFk5H-7ZXpBLY2EL72pqrMJRA6Y2R3
"""


def solution(input_str):
    new_str = input_str.split()
    new_list = []
   
    for x in new_str:
        if x not in new_list:
            new_list.append(x)
                   
    return " ".join(new_list)