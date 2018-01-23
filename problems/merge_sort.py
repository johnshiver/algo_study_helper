INSTRUCTIONS = """

Given an unsorted array of integers, write a merge sort implementation
to sort them.

"""

from utils.decorators import time_this

@time_this
def solution(inputs):
    return merge_sort(inputs)

def merge_sort(unsorted_array):
    #import ipdb;ipdb.set_trace()

    if len(unsorted_array) < 2:
        return unsorted_array

    mid = len(unsorted_array) / 2
    mid = int(mid)
    left = unsorted_array[:mid]
    right = unsorted_array[mid:]
    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left, right):
    l, r = 0, 0
    final = []
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            final.append(left[l])
            l += 1
        else:
            final.append(right[r])
            r += 1

    while l < len(left):
        final.append(left[l])
        l += 1

    while r < len(right):
        final.append(right[r])
        r += 1

    return final


def generate_test_case_inputs():
    import random
    return [[random.randrange(100000) for _ in range(100)]
            for _ in range(100)]


test_case_inputs = generate_test_case_inputs()
