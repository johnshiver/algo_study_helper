INSTRUCTIONS = """
Thanks leetcode: https://leetcode.com/problems/number-of-1-bits/description/

Write a function that takes an unsigned integer and returns the number of ’1' bits it has (also known as the Hamming weight).

For example, the 32-bit integer ’11' has binary representation 00000000000000000000000000001011, so the function should return 3
"""

from utils.decorators import time_this

@time_this
def solution(inputs):
    """
	"""
    n = inputs
    count = 0
    while n:
        # adds 1 to count if right most bit is 1
        count += n & 1
        # shift bits to right by 1
        n >>= 1
    return count



import random
test_case_inputs = [random.randrange(1, 10000000) for _ in range(10000)]
