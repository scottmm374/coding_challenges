
def singleNumber( nums):
#         using XOR operator
    result = 0
    for x in nums:
        result = x ^ result
    return result



    # Runtime beats 61.70%   174 ms
    # Space beats 50.50%  Memory Usage 16.7mb
    # 61/61 test cases pass