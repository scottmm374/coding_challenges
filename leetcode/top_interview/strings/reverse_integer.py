
import math

def reverse(x):
    j = math.pow(2, 31)

    if x < 0:
        negative_convert = abs(x)
        number = str(negative_convert)
        reversed_string = number[::-1]
        reversed_int = (int(reversed_string))
        if reversed_int > j:
            return 0
        return -abs(reversed_int)

    number = str(x)
    reversed_string = number[::-1]
    reversed_int = (int(reversed_string))
    if reversed_int > j:
            return 0
    return reversed_int
