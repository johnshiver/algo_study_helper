INSTRUCTIONS = """
Given a number and a sorted array, perform binary search to find the index
of the given number.

All numbers will occur exactly once.

If the number is not in the given array, return the string 'not found'
"""

from utils.decorators import time_this

@time_this
def solution(inputs):
	num, array = inputs
	return binary_search(array, num, 0, len(array)-1)

def binary_search(array, num, start, end):
    if start <= end:
        mid = (start + end) / 2
        mid = int(mid)
        if array[mid] == num:
            return mid
        elif array[mid] < num:
            return binary_search(array, num, mid+1, end)
        else:
            return binary_search(array, num, 0, mid-1)
    else:
        return "not found"


def generate_random_test_case():
    import random
    array = [random.randrange(1, 1000000) for _ in range(100)]
    array = sorted(list(set(array)))
    if (random.random() * 10) < 6:
        num = random.randint(1, len(array)-1)
    else:
        num = 23098234082340
    return (num, array)


test_case_inputs = [generate_random_test_case() for _ in range(1000)]
