"""
Create a function that given an integer, returns an integer where every digit in the input integer is squared.

Examples:

    solution(9119) -> 811181 because 9^2 = 81, 1^2 = 1, 1^2 = 1, and 9^2 = 81
    solution(2483) -> 416649 because 2^2 = 4, 4^2 = 16, 8^2 = 64, and 3^2 = 9

    [execution time limit] 4 seconds (py3)

    [input] integer n

    [output] integer

https://app.codesignal.com/solutions/TtFtFTQTfwfE9MaZt?accessToken=riSN79DwWmRmwFk5H-oSMFqzhcyL2ZqgZPNFLE9xwZ

"""


def solution(n):
    square_list = []
    for digit in str(n):
        square_list.append(str(int(digit) ** 2))

    return int(''.join(square_list))